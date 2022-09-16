from telnetlib import DO
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from tkinter import font
from PIL import ImageFont
from turtle import color
import customtkinter
import sqlite3
from re import fullmatch
from re import compile
from re import match


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor T")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.loginPage()

    ############## Checking User Info #############################

    def loginUser(self):
        flag = 0
        conn = sqlite3.connect("records.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM account")
        user = self.username.get()
        pwd = self.password.get()
        accounts = cursor.fetchall()
        for account in accounts:
            flag = 0
            if user in account:
                flag = 1
                if pwd == account[1]:
                    SuccessLabel = customtkinter.CTkLabel(self.frame, text = "Login Successful", bg_color = "black", text_color = "red")
                    SuccessLabel.grid(column = 0, columnspan = 2, row = 4, pady = (15, 0))          
                else:
                    InvalidLabel = customtkinter.CTkLabel(self.frame, text = "Invalid Username or Password.", bg_color = "black", text_color = "red")
                    InvalidLabel.grid(column = 0, columnspan = 2, row = 4, pady = (15, 0)) 
                    break
        if flag == 0:
            FlagLabel = customtkinter.CTkLabel(self.frame, text = "Invalid Username or Password.", bg_color = "black", text_color = "red")
            FlagLabel.grid(column = 0, columnspan = 2, row = 4, pady = (15, 0)) 
        conn.close()
    

    ################## Function for registering new user ######################

    def registerUser(self):
        self.usr1 = self.email.get()
        self.pwd1 = self.pwd.get()
        self.ret1 = self.retype.get() 

        self.regex = compile("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")

        self.conn = sqlite3.connect("records.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM account")
        records = self.cursor.fetchall()
        for record in records:
            if self.usr1 in record:
                ExistLabel = customtkinter.CTkLabel(self.frame, text = "This Email Is Already Registered. Try Logging In.", bg_color = "black", text_color = "red")
                ExistLabel.grid(column = 0, columnspan = 2, row = 4)
                return 
        if fullmatch(self.regex, self.usr1):
            DoneLabel = customtkinter.CTkLabel(self.frame, text = "Registration Successful", bg_color = "black", text_color = "red")
            DoneLabel.grid(column = 0, columnspan = 2, row = 4)
            self.cursor.execute("INSERT INTO account VALUES(?, ?)", (self.usr1, self.pwd1))
            self.conn.commit()
            self.conn.close()
        else:
            InvalidLabel = customtkinter.CTkLabel(self.frame, text = "Invalid Email Address", bg_color = "black", text_color = "red")
            InvalidLabel.grid(column = 0, columnspan = 2, row = 4)
        if self.pwd1 != self.ret1:
            PassLabel = customtkinter.CTkLabel(self.frame, text = "Passwords Do Not Match.", bg_color = "black", text_color = "red")
            PassLabel.grid(column = 0, columnspan = 2, row = 4)

    ###################### Login Page ##############################

    def loginPage(self):
        for i in self.root.winfo_children():
            i.destroy()

        self.font1 = ImageFont.truetype("pacfont.ttf", 25)
        
        
        self.C = Canvas(self.root, bg="blue", height=250, width=300)
        self.filename = PhotoImage(file = "background.png")
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = customtkinter.CTkFrame(self.root, width = 750, height = 750, bg_color = "black")


        # Title Label
        self.TitleLabel = customtkinter.CTkLabel(self.frame, text = "Doctor T", text_color = "#0096FF")
        self.TitleLabel.configure(font = ("PacFont", 25))
        self.TitleLabel.grid(column = 0, row = 1, columnspan = 2, pady = (25, 25))


        # Username and Entry Box
        self.Label1 = customtkinter.CTkLabel(self.frame, text = "Username")
        self.Label1.grid(column = 0, row = 2, pady = (25, 0), padx = (25, 0))
        self.username = customtkinter.CTkEntry(self.frame, width = 350)
        self.username.grid(column = 1, row = 2, pady = (25, 0), padx = (0, 100))


        # Password and Entry Box
        self.Label2 = customtkinter.CTkLabel(self.frame, text = "Password")
        self.Label2.grid(column = 0, row = 3, pady = (25, 0), padx = (25, 0))
        self.password = customtkinter.CTkEntry(self.frame, width = 350, show = "*")
        self.password.grid(column = 1, row = 3, pady = (25, 0), padx = (0, 100))  

        # Login Button
        self.Button1 = customtkinter.CTkButton(self.frame, text = "Log In", command = self.loginUser)
        self.Button1.grid(row = 5, column = 0, pady = (50, 40), padx = (150, 0), sticky = NE)

        # Register Button
        self.Button2 = customtkinter.CTkButton(self.frame, text = "Register", command = self.registerPage)
        self.Button2.grid(row = 5, column = 1, pady = (50, 40))

        self.frame.pack(padx = 30, pady = 100)
        self.C.pack()
        # self.root.eval('tk::PlaceWindow . center')

    ##################### NEW USER REGISTRATION PAGE ##################################

    def registerPage(self):
        for i in self.root.winfo_children():
            i.destroy()
        

        self.C = Canvas(root, bg="blue", height=200, width=300)
        self.filename = PhotoImage(file = "background.png")
        self.background_label = Label(root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = customtkinter.CTkFrame(root, width = 750, height = 750, bg_color = "black")


        # Heading Of The Registration Page
        self.TitleLabel = customtkinter.CTkLabel(self.frame, text = "New User? Register Now!", text_color = "#0096FF")
        self.TitleLabel.configure(font = ("Pacifico", 25))
        self.TitleLabel.grid(column = 0, row = 0, columnspan = 2, pady = (25, 25), padx = (25, 25), sticky = NS)


        # Email Label
        self.EmailLabel = customtkinter.CTkLabel(self.frame, text = "New User Email:")
        self.EmailLabel.grid(column = 0, row = 1, padx = (0, 0), pady = (20, 20))

        # Email Entry
        self.email = customtkinter.CTkEntry(self.frame, width = 250)
        self.email.grid(column = 1, row = 1, pady= (20, 20))

        # Password Label
        self.PassLabel = customtkinter.CTkLabel(self.frame, text = "Enter Password:")
        self.PassLabel.grid(column = 0, row = 2, padx = (0, 0), pady = (20, 0))

        # Password Entry
        self.pwd = customtkinter.CTkEntry(self.frame, width = 250, show = "*")
        self.pwd.grid(column = 1, row = 2, pady = (20, 0))

        # Password Label
        self.RetypeLabel = customtkinter.CTkLabel(self.frame, text = "Retype Password:")
        self.RetypeLabel.grid(column = 0, row = 3, padx = (0, 0), pady = (20, 20))

        # Password Entry
        self.retype = customtkinter.CTkEntry(self.frame, width = 250, show = "*")
        self.retype.grid(column = 1, row = 3, pady = (20, 20))

        # Register Button
        self.register = customtkinter.CTkButton(self.frame, text = "Register Now", command = self.registerUser)
        self.register.grid(column = 0, columnspan = 2, row = 5, pady = (30, 20)) 

        # Back To Sign In Button
        backsign = customtkinter.CTkButton(self.frame, text = "Back To Sign In", command = self.loginPage)
        backsign.grid(column = 0, columnspan = 2, row = 6, pady = (0, 20)) 

        self.frame.pack(padx = 30, pady = 100)
        self.C.pack()
        # root.eval('tk::PlaceWindow . center')






root = Tk()
App(root)
root.mainloop()



