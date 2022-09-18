from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from tkinter import font
from PIL import ImageFont
from turtle import color
import customtkinter
import sqlite3

################ DATABASE CODE BEGINS #####################################

# Function for Validating user
def loginUser():
    flag = 0
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM account")
    user = username.get()
    pwd = password.get()
    accounts = cursor.fetchall()
    for account in accounts:
        flag = 0
        if user in account:
            flag = 1
            if pwd == account[1]:
                print("Login Successful.")          
            else:
                print("Wrong Password.")
            break
    if flag == 0:
        print("Record not Found.")
    

################## DATABASE CODE ENDS ######################################

root = Tk()
root.title("Doctor T")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

font1 = ImageFont.truetype("pacfont.ttf", 25)

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "background.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = customtkinter.CTkFrame(root, width = 750, height = 750, bg_color = "black")

# frame.columnconfigure(0, weight = 1)
frame.columnconfigure(1, weight = 2)



# Title Label
TitleLabel = customtkinter.CTkLabel(frame, text = "Doctor T", text_color = "#0096FF")
TitleLabel.configure(font = ("PacFont", 25))
TitleLabel.grid(column = 1, row = 1, pady = (25, 25), padx = (0, 275))


# Username and Entry Box
Label1 = customtkinter.CTkLabel(frame, text = "Username")
Label1.grid(column = 0, row = 2, pady = (25, 0), padx = (25, 0))
username = customtkinter.CTkEntry(frame, width = 350)
username.grid(column = 1, row = 2, pady = (25, 0), padx = (0, 100))

# Space between Username and Password
SpaceLabel = customtkinter.CTkLabel(frame, text = "")
SpaceLabel.grid(column = 0, row = 3)

# Password and Entry Box
Label2 = customtkinter.CTkLabel(frame, text = "Password")
Label2.grid(column = 0, row = 4, pady = (25, 0), padx = (25, 0))
password = customtkinter.CTkEntry(frame, width = 350, show = "*")
password.grid(column = 1, row = 4, pady = (25, 0), padx = (0, 100))  

# Space between Password row and Bottom of the frame
SpaceLabel = customtkinter.CTkLabel(frame, text = "\n")
SpaceLabel.grid(row = 5, column = 0)
SpaceLabel.grid(row = 6, column = 0)

# Login Button
Button1 = customtkinter.CTkButton(frame, text = "Log In", command = loginUser)
Button1.grid(row = 7, column = 0, pady = (20, 40), padx = (150, 0))

# Register Button
Button2 = customtkinter.CTkButton(frame, text = "Register")
Button2.grid(row = 7, column = 1, pady = (20, 40), padx = (0, 100))



# Space between right and the rest of the frame
# frame.columnconfigure(3, weight = 0)
# SpaceLabel = customtkinter.CTkLabel(frame, text = "")
# SpaceLabel.grid(column = 5)





frame.pack(padx = 30, pady = 150)
C.pack()
root.eval('tk::PlaceWindow . center')
root.mainloop()