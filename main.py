from tkinter import *
from PIL import ImageTk

def on_entry_click(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, END)
        entry.config(fg='#C2272D')  # Change text color to desired color
        canvas.delete("underline")

def on_entry_leave(entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')  # Change text color to grey or any other color
        canvas.delete("underline")

def draw_underline(widget, color="#5F7C8D"):
    x1, y1, x2, y2 = widget.winfo_rootx(), widget.winfo_rooty() + widget.winfo_height(), widget.winfo_rootx() + widget.winfo_width(), widget.winfo_rooty() + widget.winfo_height()
    canvas.create_line(x1, y1, x2, y2, fill=color, tags="underline")

def sign_in():
    # Add your sign-in logic here
    username = usernameEntry.get()
    password = passwordEntry.get()
    # Example: Check if the username and password are correct (replace with your authentication logic)
    if username == "your_username" and password == "your_password":
        print("Sign In Successful")
    else:
        print("Sign In Failed")

def switch_to_signup():
    root.title('SIGN UP PAGE')
    heading.config(text="SIGN UP", fg='#7A999C')
    sign_in_button.config(text="Create Account", command=sign_up)
    switch_button.config(text="Already have an account? Log In", command=switch_to_login)

def sign_up():
    # Add your sign-up logic here
    new_username = usernameEntry.get()
    new_password = passwordEntry.get()
    # Example: Save new_username and new_password to your database (replace with your sign-up logic)
    print(f"Sign Up Successful. Username: {new_username}, Password: {new_password}")

def switch_to_login():
    root.title('LOGIN PAGE')
    heading.config(text="LOG-IN", fg='#7A999C')
    sign_in_button.config(text="Log In", command=sign_in)
    switch_button.config(text="Don't have an account? Create One", command=switch_to_signup)

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
