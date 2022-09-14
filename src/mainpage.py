from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


root = customtkinter.CTk()

root.geometry("300x300")
root.title("Doctor T")


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copyImage.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    Label1.config(image = photo, borderwidth = 0)
    Label1.image = photo #avoid garbage collection

img = Image.open('background.png')
copyImage = img.copy()
photo = ImageTk.PhotoImage(img)
Label1 = ttk.Label(root, image = photo, borderwidth = 0)
Label1.bind("<Configure>", resize_image)
Label1.pack(fill = BOTH, expand = YES)



root.mainloop()