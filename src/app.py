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
from uniqueid import *




class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor T")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.radio_var = IntVar()
        self.valueMonth = [str(i) for i in range(1, 13)]
        self.valueDays = [str(i) for i in range(1, 32)]
        self.valueYears = [str(i) for i in range(1970, 2022)]
        # self.loginPage()
        self.patientEntry()
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

    ##################### Creating Patient Record ###################
    def newPatient(self):
        self.flag = 0
        self.gender1 = "None"
        self.name1 = self.name.get()
        self.height1 = self.height.get()
        self.day1 = int(self.day.get()) 
        self.month1 = int(self.month.get())
        self.year1 = int(self.year.get())

        self.unique1 = unique_id_compute(self.name1, self.year1)
    
        self.phoneRegex = compile("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")
        if fullmatch(self.phoneRegex, self.phone.get()):
            self.phone1 = self.phone.get()
        else:
            self.ErrorLabel = customtkinter.CTkLabel(self.frame, text = "Invalid Phone Number", bg_color = "#FF3131")
            self.ErrorLabel.grid(column = 2, row = 2, pady = (0, 25))
            self.flag = 1
    
        self.weightRegex = compile("^([0-9]{2,3})")
        if fullmatch(self.weightRegex, self.weight.get()):
            self.weight1 = self.weight.get()
        else:
            self.ErrorLabel = customtkinter.CTkLabel(self.frame, text = "Invalid Weight", bg_color = "#FF3131")
            self.ErrorLabel.grid(column = 2, row = 3, pady = (0, 25))
            self.flag = 1

        self.heightRegex = compile("^([0-9]{2,3})")
        if fullmatch(self.heightRegex, self.height.get()):
            self.height1 = self.height.get()
        else:
            self.ErrorLabel = customtkinter.CTkLabel(self.frame, text = "Invalid Height", bg_color = "#FF3131")
            self.ErrorLabel.grid(column = 2, row = 4, pady = (0, 25))
            self.flag = 1

        if self.radio_var == 1:
            gender1 = "Male"
        elif self.radio_var == 2:
            gender1 = "Female"
        elif self.radio_var == 3:
            gender1 = "Non-Binary"
    
        if self.flag == 0:
            self.conn = sqlite3.connect("records.db")
            self.cursor = self.conn.cursor()
            self.cursor.execute("INSERT INTO patient_list VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.unique1, self.name1, self.phone1, self.weight1, self.height1, self.gender1, self.day1, self.month1, self.year1))
            self.conn.commit()
            self.conn.close()
            self.BaseLabel.destroy()
            SuccessLabel = customtkinter.CTkLabel(self.frame, text = "Unique ID:" + self.unique1, bg_color = "#FF3131")
            SuccessLabel.grid(row = 9, column = 3, padx = (0, 25))
        return




    ###################### Login Page ################################

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


################################ Patient Data Entry Page #############################################


    def patientEntry(self):
        for i in self.root.winfo_children():
            i.destroy()

        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("blue")

        self.filename = PhotoImage(file = "smaller.png")
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.frame = customtkinter.CTkFrame(root, width = 1500, height = 2000, bg_color = "white")

        self.FormTitleLabel = customtkinter.CTkLabel(self.frame, text = "New Patient Form", text_color = "#FF3131")
        self.FormTitleLabel.configure(font = ("Pacifico", 25))
        self.FormTitleLabel.grid(column = 0, columnspan = 6, row = 0, sticky = N, padx = (150, 100), pady = (25, 25))

        self.NameLabel = customtkinter.CTkLabel(self.frame, text = "Name")
        self.NameLabel.configure(font = ("Helvetica", 12))
        self.NameLabel.grid(column = 0, row = 1, padx = (0, 50), pady = (25, 25))

        self.name = customtkinter.CTkEntry(self.frame, width = 300, placeholder_text = "Enter Patient Name")
        self.name.grid(column = 4, row = 1, columnspan = 2, padx = (10, 10), pady = (25, 25))

        self.PhoneLabel = customtkinter.CTkLabel(self.frame, text = "Phone")
        self.PhoneLabel.configure(font = ("Helvetica", 12))
        self.PhoneLabel.grid(column = 0, row = 2, padx = (0, 50), pady = (0, 25))

        self.phone = customtkinter.CTkEntry(self.frame, width = 300, placeholder_text = "Enter Patient Phone Number")
        self.phone.grid(column = 4, row = 2, columnspan = 2, padx = (10, 10), pady = (0, 25))

        self.WeightLabel = customtkinter.CTkLabel(self.frame, text = "Weight")
        self.WeightLabel.configure(font = ("Helvetica", 12))
        self.WeightLabel.grid(column = 0, row = 3, padx = (0, 50), pady = (0, 25))

        self.weight = customtkinter.CTkEntry(self.frame, width = 300, placeholder_text = "Enter Patient Weight In KGs")
        self.weight.grid(column = 4, row = 3, columnspan = 2, padx = (10, 10), pady = (0, 25))

        self.HeightLabel = customtkinter.CTkLabel(self.frame, text = "Height")
        self.HeightLabel.configure(font = ("Helvetica", 12))
        self.HeightLabel.grid(column = 0, row = 4, padx = (0, 50), pady = (0, 25))

        self.height = customtkinter.CTkEntry(self.frame, width = 300, placeholder_text = "Enter Patient Height In Cm")
        self.height.grid(column = 4, row = 4, columnspan = 2, padx = (10, 10), pady = (0, 25))


        self.GenderLabel = customtkinter.CTkLabel(self.frame, text = "Gender")
        self.GenderLabel.configure(font = ("Helvetica", 12))
        self.GenderLabel.grid(column = 0, row = 5, padx = (0, 50), pady = (25, 25))

        self.male = customtkinter.CTkRadioButton(self.frame, text = "Male", border_color ="#FF3131", fg_color = "#FF3131", variable = self.radio_var, value = 1)
        self.male.grid(column = 2, row = 5, pady = (25, 25))

        self.female = customtkinter.CTkRadioButton(self.frame, text = "Female", border_color = "#FF3131", fg_color = "#FF3131", variable = self.radio_var, value = 2)
        self.female.grid(column = 3, row = 5, pady = (25, 25))

        self.nonbinary = customtkinter.CTkRadioButton(self.frame, text = "Non-Binary", border_color = "#FF3131", fg_color = "#FF3131", variable = self.radio_var, value = 3)
        self.nonbinary.grid(column = 4, row = 5, pady = (25, 25), padx = (0, 75))

        self.DayLabel = customtkinter.CTkLabel(self.frame, text = "Day")
        self.DayLabel.configure(font = ("Helvetica", 12))
        self.DayLabel.grid(column = 0, row = 6, padx = (0, 50), pady = (0, 0))

        self.day = customtkinter.CTkOptionMenu(self.frame, values = self.valueDays, fg_color = "white", button_color = "#FF3131")
        self.day.grid(column = 4, row = 6, pady = (25, 25))

        self.MonthLabel = customtkinter.CTkLabel(self.frame, text = "Month")
        self.MonthLabel.configure(font = ("Helvetica", 12))
        self.MonthLabel.grid(column = 0, row = 7, padx = (0, 50), pady = (0, 25))

        self.month = customtkinter.CTkOptionMenu(self.frame, values = self.valueMonth, fg_color = "white", button_color = "#FF3131")
        self.month.grid(column = 4, row = 7, pady = (0, 25))

        self.yearLabel = customtkinter.CTkLabel(self.frame, text = "Year Of Birth")
        self.yearLabel.configure(font = ("Helvetica", 12))
        self.yearLabel.grid(column = 0, row = 8, padx = (0, 50), pady = (0, 25))

        self.year = customtkinter.CTkOptionMenu(self.frame, values = self.valueYears, fg_color = "white", button_color = "#FF3131")
        self.year.grid(column = 4, row = 8, pady = (0, 25))

        self.BaseLabel = customtkinter.CTkLabel(self.frame, text = "Complete The Form", bg_color="#0096FF")
        self.BaseLabel.grid(row = 9, column = 3)

        self.CreateButton = customtkinter.CTkButton(self.frame, text = "Create Record", fg_color = "#FF3131", command = self.newPatient)
        self.CreateButton.grid(column = 2, row = 10, pady = (25, 25))

        self.BackButton = customtkinter.CTkButton(self.frame, text = "Search Records", fg_color = "#FF3131")
        self.BackButton.grid(column = 4, row = 10, pady = (25, 25))

        self.frame.pack(padx = 30, pady = 30)


root = Tk()
App(root)
root.mainloop()



