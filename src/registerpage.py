from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from tkinter import font
from PIL import ImageFont
from turtle import color
import customtkinter
import sqlite3
import re

################ DATABASE CODE BEGINS #####################################

# Function for registering new user
def registerUser():
    usr1 = email.get()
    pwd1 = pwd.get()
    ret1 = retype.get() 

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM account")
    records = cursor.fetchall()
    for record in records:
        if usr1 in record:
            ExistLabel = customtkinter.CTkLabel(frame, text = "This Email Is Already Registered. Try Logging In.", bg_color = "black", text_color = "red")
            ExistLabel.grid(column = 0, columnspan = 2, row = 4)
            return 
        elif (re.fullmatch(regex, usr1)) != 1:
            FullMatch = customtkinter.CTkLabel(frame, text = "Invalid Email ID. Enter A Valid Email ID to continue.", bg_color = "black", text_color = "red")
            FullMatch.grid(column = 0, columnspan = 2, row = 4)
            return
        elif pwd1 != ret1:
            PassLabel = customtkinter.CTkLabel(frame, text = "Passwords Do Not Match.", bg_color = "black", text_color = "red")
            PassLabel.grid(column = 0, columnspan = 2, row = 4)
            return
    cursor.execute("INSERT INTO account VALUES(?, ?)", (usr1, pwd1))
    conn.commit()
    conn.close()

################## DATABASE CODE ENDS ######################################

root = Tk()
root.title("Doctor T")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

font1 = ImageFont.truetype("pacfont.ttf", 25)

C = Canvas(root, bg="blue", height=200, width=300)
filename = PhotoImage(file = "background.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = customtkinter.CTkFrame(root, width = 750, height = 750, bg_color = "black")


# Heading Of The Registration Page
TitleLabel = customtkinter.CTkLabel(frame, text = "New User? Register Now!", text_color = "#0096FF")
TitleLabel.configure(font = ("Pacifico", 25))
TitleLabel.grid(column = 0, row = 0, columnspan = 2, pady = (25, 25), padx = (25, 25), sticky = NS)


# Email Label
EmailLabel = customtkinter.CTkLabel(frame, text = "New User Email:")
EmailLabel.grid(column = 0, row = 1, padx = (0, 0), pady = (20, 20))

# Email Entry
email = customtkinter.CTkEntry(frame, width = 250)
email.grid(column = 1, row = 1, pady= (20, 20))

# Password Label
PassLabel = customtkinter.CTkLabel(frame, text = "Enter Password:")
PassLabel.grid(column = 0, row = 2, padx = (0, 0), pady = (20, 0))

# Password Entry
pwd = customtkinter.CTkEntry(frame, width = 250, show = "*")
pwd.grid(column = 1, row = 2, pady = (20, 0))

# Password Label
RetypeLabel = customtkinter.CTkLabel(frame, text = "Retype Password:")
RetypeLabel.grid(column = 0, row = 3, padx = (0, 0), pady = (20, 20))

# Password Entry
retype = customtkinter.CTkEntry(frame, width = 250, show = "*")
retype.grid(column = 1, row = 3, pady = (20, 20))

# Register Button
register = customtkinter.CTkButton(frame, text = "Register Now", command = registerUser)
register.grid(column = 0, columnspan = 2, row = 5, pady = (30, 20)) 

# Back To Sign In Button
backsign = customtkinter.CTkButton(frame, text = "Back To Sign In", command = registerUser)
backsign.grid(column = 0, columnspan = 2, row = 6, pady = (0, 20)) 

frame.pack(padx = 30, pady = 100)
C.pack()
root.eval('tk::PlaceWindow . center')
root.mainloop()