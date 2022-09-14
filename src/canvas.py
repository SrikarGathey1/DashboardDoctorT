from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from turtle import color
import customtkinter


root = Tk()
root.title("Doctor T")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "background.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = customtkinter.CTkFrame(root, width = 1000, height = 1000)
frame['padding'] = (10, 10, 10, 10)
frame.columnconfigure(0, weight = 1)
frame.columnconfigure(0, weight = 3)

Label7 = customtkinter.CTkLabel(frame, text = "      ")
Label7.grid(column = 0, row = 0)

Label1 = customtkinter.CTkLabel(frame, text = "Username")
Label1.grid(column = 0, row = 1)
username = customtkinter.CTkEntry(frame, width = 150)
username.grid(column = 2, row = 1)

Label2 = customtkinter.CTkLabel(frame, text = "Password")
Label2.grid(column = 0, row = 3)
password = customtkinter.CTkEntry(frame, width = 150)
password.grid(column = 2, row = 3)  

Label3 = customtkinter.CTkLabel(frame, text = "      ")
Label3.grid(column = 1, row = 4)


frame.pack(padx = 30, pady = 30)
C.pack()
root.eval('tk::PlaceWindow . center')
root.mainloop()