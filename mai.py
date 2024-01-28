from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import hashlib
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import random
import math

def on_entry_click(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, END)
        entry.config(fg='#5F7C8D')  # Change text color to the desired color
        canvas.delete("underline")

def on_entry_leave(entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')  # Change text color to grey or any other color
        canvas.delete("underline")

def draw_underline(widget, color="#5F7C8D"):
    x1, y1, x2, y2 = widget.winfo_rootx(), widget.winfo_rooty() + widget.winfo_height(), widget.winfo_rootx() + widget.winfo_width(), widget.winfo_rooty() + widget.winfo_height()
    canvas.create_line(x1, y1, x2, y2, fill=color, tags="underline")

def hash_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def sign_in():
    username = usernameEntry.get()
    password = hash_password(passwordEntry.get())

    try:
        # Connect to SQLite database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Check if the username and hashed password match a record in the database
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            create_main_page(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    except sqlite3.Error as e:
        messagebox.showerror("SQLite Error", str(e))
    finally:
        # Close database connection
        conn.close()

def create_main_page(username):
    # Destroy existing widgets
    destroy_widgets()

    # Key Generation Button
    key_generation_button = Button(root, text="Key Generation", font=("Arial", 14), command=generate_keys, fg='#FFFFFF', bg='#4B687A', width=15)
    key_generation_button.place(x=250, y=400)

    # Encryption Button
    encryption_button = Button(root, text="Encryption", font=("Arial", 14), command=perform_encryption, fg='#FFFFFF', bg='#4B687A', width=15)
    encryption_button.place(x=550, y=400)

    # Decryption Button
    decryption_button = Button(root, text="Decryption", font=("Arial", 14), command=perform_decryption, fg='#FFFFFF', bg='#4B687A', width=15)
    decryption_button.place(x=850, y=400)

    # Result Label
    result_label = Label(root, text="", font=("Arial", 14), fg='#000000', bg='#FFFFFF')
    result_label.place(x=400, y=500)

def generate_keys():
    p = getPrime(128)
    q = getPrime(128)
    r = 12345  # Some constant value for microseconds_part

    n = p * q * r
    phi = (p - 1) * (q - 1) * (r - 1)
    e = random.randrange(2, phi)
    while math.gcd(phi, e) != 1:
        e = random.randrange(2, phi)
    d = pow(e, -1, phi)

    result_label.config(text=f"Public Key: {n}, {e}\nPrivate Key: {n}, {d}")

def perform_encryption():
    key_n = int(input("Enter the public key 'n': "))
    key_e = int(input("Enter the public key 'e': "))
    message = input("Enter the Text to Encrypt: ")

    encrypted = encrypt(key_n, key_e, message)
    result_label.config(text=f"Encrypted Message: {encrypted}")

def perform_decryption():
    key_n = int(input("Enter the private/public key 'n': "))
    key_d = int(input("Enter the private key 'd': "))
    encrypted = int(input("Enter the Encrypted Message: "))

    decrypted = decrypt(key_n, key_d, encrypted)
    result_label.config(text=f"Decrypted Message: {decrypted}")

def encrypt(n, e, message):
    return pow(bytes_to_long(message.encode()), e, n)

def decrypt(n, d, encrypted):
    return long_to_bytes(pow(encrypted, d, n)).decode()

def switch_to_signup():
    root.title('SIGN UP PAGE')
    heading.config(text="SIGN UP", fg='#7A999C')
    sign_in_button.config(text="Create Account", command=sign_up)
    switch_button.config(text="Already have an account? Log In", command=switch_to_login)
    clear_entries()

def sign_up():
    new_username = usernameEntry.get()
    new_password = hash_password(passwordEntry.get())

    try:
        # Connect to SQLite database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username=?", (new_username,))
        existing_user = cursor.fetchone()

        if existing_user:
            messagebox.showerror("Username Exists", "Username already exists. Choose a different username.")
        else:
            # Insert new user into the database
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, new_password))
            conn.commit()
            switch_to_login()

    except sqlite3.Error as e:
        messagebox.showerror("SQLite Error", str(e))
    finally:
        # Close database connection
        conn.close()

def switch_to_login():
    root.title('LOGIN PAGE')
    heading.config(text="LOG-IN", fg='#7A999C')
    sign_in_button.config(text="Log In", command=sign_in)
    switch_button.config(text="Don't have an account? Create One", command=switch_to_signup)
    clear_entries()

def clear_entries():
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)

def destroy_widgets():
    # Destroy all widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()

# Create SQLite database table if not exists
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')
conn.close()

root = Tk()
root.resizable(0, 0)
root.title('LOGIN PAGE')

# Background image
bgImg = ImageTk.PhotoImage(file="R.jpg")
bgLabel = Label(root, image=bgImg)
bgLabel.grid(row=0, column=0)

# ---------------------------
bgImg2 = ImageTk.PhotoImage(file="fig.png")
bgLabel2 = Label(root, image=bgImg2)
bgLabel2.place(x=0, y=0)

# Heading
heading = Label(root, text="
