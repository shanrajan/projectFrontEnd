from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import hashlib
from tkinter import messagebox

def on_entry_click(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, END)
        entry.config(fg='#5F7C8D')  # Change text color to desired color
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


    # Profile Button
    profile_button = Button(root, text="Keygeneration", font=("Arial", 14), fg='#FFFFFF', bg='#4B687A', width=15)
    profile_button.place(x=250, y=400)

    # Settings Button
    settings_button = Button(root, text="Encryption", font=("Arial", 14), fg='#FFFFFF', bg='#4B687A', width=15)
    settings_button.place(x=550, y=400)

    # Logout Button
    logout_button = Button(root, text="Decryption", font=("Arial", 14), fg='#FFFFFF', bg='#4B687A', width=15)
    logout_button.place(x=850, y=400)

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
heading = Label(root, text="LOG-IN", font=("Arial", 23, "bold"), fg='#7A999C', bg='#FFFFFF')  # Set background color to white
heading.place(x=850, y=225)

# Username Entry
usernamePlaceholder = "Username"
usernameEntry = Entry(root, width=25, font=("anton", 13, "bold"), bd=0, fg='#5F7C8D')
usernameEntry.insert(0, usernamePlaceholder)
usernameEntry.bind("<FocusIn>", lambda event: on_entry_click(usernameEntry, usernamePlaceholder))
usernameEntry.bind("<FocusOut>", lambda event: on_entry_leave(usernameEntry, usernamePlaceholder))
usernameEntry.place(x=800, y=325)
canvas = Canvas(root, highlightthickness=0, bg=root['bg'])
canvas.place(x=800, y=345, width=230, height=2)  # Adjusted y-coordinate and height

# Password Entry
passwordPlaceholder = "Password"
passwordEntry = Entry(root, width=25, font=("anton", 13, "bold"), bd=0, show='*', fg='#5F7C8D')
passwordEntry.insert(0, passwordPlaceholder)
passwordEntry.bind("<FocusIn>", lambda event: on_entry_click(passwordEntry, passwordPlaceholder))
passwordEntry.bind("<FocusOut>", lambda event: on_entry_leave(passwordEntry, passwordPlaceholder))
passwordEntry.place(x=800, y=425)
canvas = Canvas(root, highlightthickness=0, bg=root['bg'])
canvas.place(x=800, y=445, width=230, height=2)  # Adjusted y-coordinate and height

# Sign In Button (with increased width)
sign_in_button = Button(root, text="Log In", command=sign_in, font=("Arial", 14, "bold"), fg='#FFFFFF', bg='#4B687A', width=15)
sign_in_button.place(x=815, y=525)  # Adjusted y-coordinate

# Switch Button
switch_button = Button(root, text="Don't have an account? Create One", command=switch_to_signup, font=("Arial", 12), fg='#5F7C8D', bg='#FFFFFF')
switch_button.place(x=790, y=600)

root.mainloop()
