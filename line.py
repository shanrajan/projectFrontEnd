from tkinter import *
from PIL import ImageTk

root = Tk()
root.resizable(0, 0)
root.title('MAIN PAGE')

# Background image
bgImg = ImageTk.PhotoImage(file="R.jpg")
bgLabel = Label(root, image=bgImg)
bgLabel.grid(row=0, column=0)

# Profile Button
key_generation_button = Button(root, text="Keygeneration", font=("Arial", 14), fg='#FFFFFF', bg='#4B687A', width=15)
key_generation_button.place(x=250, y=400)

Encryption_button = Button(root, text="Encryption", font=("Arial", 14), fg='#FFFFFF', bg='#4B687A', width=15)
Encryption_button.place(x=550, y=400)

Decryption_button = Button(root, text="Decryption", font=("Arial", 14), fg='#FFFFFF', bg='#4B687A', width=15)
Decryption_button.place(x=850, y=400)

root.mainloop()
