from tkinter import *
import customtkinter

root = Tk()

def removeLabel(Label):
    Label.grid_remove()
 
def showLabel(Label, x, y):
    Label.grid(column = y, columnspan = 2, row = x)


Button1 = customtkinter.CTkButton(root, text = "Remove", command = lambda: removeLabel(Label1))
Button1.grid(column = 0, row = 0)

Button2 = customtkinter.CTkButton(root, text = "Show", command = lambda: showLabel(Label1, 1, 0))
Button2.grid(column = 1, row = 0)

Label1 = customtkinter.CTkLabel(root, text = "Acharya Bossobhava.")
Label1.grid(column = 1, columnspan = 2, row = 1)

root.mainloop()