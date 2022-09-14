from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()


frame = customtkinter.CTkFrame(root, width = 200, height = 200, bg_color = "red", border_color="green")
frame.pack(padx = 100, pady = 100, anchor = CENTER)

Label1 = customtkinter.CTkLabel(frame, text = "Username", fg_color = "black")
Label1.pack(anchor = CENTER)

Label2 = customtkinter.CTkLabel(frame, text = "Password", fg_color = "black")
Label2.pack()


root.mainloop()

