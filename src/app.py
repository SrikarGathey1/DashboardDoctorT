from telnetlib import DO
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from tkinter import font
from PIL import ImageFont, ImageTk, Image
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
        self.loginPage()
        # self.patientEntry()
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
                    self.searchPage()          
                else:
                    InvalidLabel = customtkinter.CTkLabel(self.LoginFrame, text = "Invalid Username or Password.", bg_color = "black", text_color = "red")
                    InvalidLabel.grid(column = 0, columnspan = 2, row = 4, pady = (15, 0)) 
                    break
        if flag == 0:
            self.FlagLabel = customtkinter.CTkLabel(self.LoginFrame, text = "Invalid Username or Password.", bg_color = "black", text_color = "red")
            self.FlagLabel.grid(column = 0, columnspan = 2, row = 4, pady = (15, 0)) 
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

    ###################### Search Page Database ######################

    def searchRecords(self, searchStr): 
        for widget in self.ResultInterFrame.winfo_children():
            widget.destroy()

        self.searchResults = []
        self.conn = sqlite3.connect("records.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM patient_list")
        self.items = self.cursor.fetchall()
        for item in self.items:
            self.name = item[1]
            self.phone = str(item[2])
            if searchStr in item[1]:
                if item in self.searchResults:
                    continue
                else:
                    self.searchResults.append(item)
            if searchStr in self.phone:
                if item in self.searchResults:
                    continue
                else:
                    self.searchResults.append(item)
            if searchStr in item[0]:
                if item in self.searchResults:
                    continue
                self.searchResults.append(item)
        index = 0
        for item in self.searchResults:
            UniqueLabel = customtkinter.CTkLabel(self.ResultInterFrame, text = item[0])
            UniqueLabel.configure(font = ("Oswald", 10))
            UniqueLabel.grid(row = index, column = 0, pady = 10, padx = 10)

            NameLabel = customtkinter.CTkLabel(self.ResultInterFrame, text = item[1])
            NameLabel.configure(font = ("Oswald", 10))
            NameLabel.grid(row = index, column = 1, pady = 10, padx = 10)

            ViewButton = customtkinter.CTkButton(self.ResultInterFrame, text = "View", text_font = ("Oswald", 10), command = lambda: self.breathAnalyze(item[0]))
            ViewButton.grid(row = index, column = 2, pady = 10, padx = 10)
            index += 1
        if len(self.searchResults) == 0:
            NotFoundLabel = customtkinter.CTkLabel(self.ResultInterFrame, text = "No records found!!")
            NotFoundLabel.configure(font = ("Oswald", 15))
            NotFoundLabel.grid(row = 0, column = 0, columnspan = 3, padx = 200, pady = 50)


    ###################### Login Page ################################

    def loginPage(self):
        for i in self.root.winfo_children():
            i.destroy()

        self.font1 = ImageFont.truetype("pacfont.ttf", 25)
        
        
        self.C = Canvas(self.root, bg="blue", height=250, width=300)
        self.filename = PhotoImage(file = "background.png")
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.LoginFrame = customtkinter.CTkFrame(self.root, width = 750, height = 750, bg_color = "black")


        # Title Label
        self.TitleLabel = customtkinter.CTkLabel(self.LoginFrame, text = "Doctor T", text_color = "#0096FF")
        self.TitleLabel.configure(font = ("PacFont", 25))
        self.TitleLabel.grid(column = 0, row = 1, columnspan = 2, pady = (25, 25))


        # Username and Entry Box
        self.Label1 = customtkinter.CTkLabel(self.LoginFrame, text = "Username")
        self.Label1.grid(column = 0, row = 2, pady = (25, 0), padx = (25, 0))
        self.username = customtkinter.CTkEntry(self.LoginFrame, width = 350)
        self.username.grid(column = 1, row = 2, pady = (25, 0), padx = (0, 100))


        # Password and Entry Box
        self.Label2 = customtkinter.CTkLabel(self.LoginFrame, text = "Password")
        self.Label2.grid(column = 0, row = 3, pady = (25, 0), padx = (25, 0))
        self.password = customtkinter.CTkEntry(self.LoginFrame, width = 350, show = "*")
        self.password.grid(column = 1, row = 3, pady = (25, 0), padx = (0, 100))  

        # Login Button
        self.Button1 = customtkinter.CTkButton(self.LoginFrame, text = "Log In", command = self.loginUser)
        self.Button1.grid(row = 5, column = 0, pady = (50, 40), padx = (150, 0), sticky = NE)

        # Register Button
        self.Button2 = customtkinter.CTkButton(self.LoginFrame, text = "Register", command = self.registerPage)
        self.Button2.grid(row = 5, column = 1, pady = (50, 40))

        self.LoginFrame.pack(padx = 30, pady = 100)
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

        self.CreateButton = customtkinter.CTkButton(self.frame, text = "Create Record", fg_color = "#FF3131", command = lambda: self.patientEntry)
        self.CreateButton.grid(column = 2, row = 10, pady = (25, 25))

        self.BackButton = customtkinter.CTkButton(self.frame, text = "Search Records", fg_color = "#FF3131", command = lambda: self.searchPage())
        self.BackButton.grid(column = 4, row = 10, pady = (25, 25))

        self.frame.pack(padx = 30, pady = 30)

########################## SEARCH PAGE ###################################################

    def searchPage(self):
        for i in self.root.winfo_children():
            i.destroy()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")


        self.filename = PhotoImage(file = "searchPage.png")
        self.background_label = Label(self.root, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.TitleFrame = customtkinter.CTkFrame(root, width = 500, height = 500, fg_color = "#6495ED")

        self.InterFrame = customtkinter.CTkFrame(self.TitleFrame, width = 460, height = 460, fg_color = "#0047AB")

        self.TitleLabel = customtkinter.CTkLabel(self.InterFrame, text = "SEARCH PATIENT RECORDS", text_color = "white")
        self.TitleLabel.configure(font = ("Oswald", 15))
        self.TitleLabel.grid(column = 0, row = 0, columnspan = 3, padx = 10, pady = 20)

        self.SearchEntry = customtkinter.CTkEntry(self.InterFrame, placeholder_text = "Search for patients", width = 150)
        self.SearchEntry.grid(column = 0, row = 1, padx = 10, pady = (0, 10))

        self.SearchButton = customtkinter.CTkButton(self.InterFrame, text = "Search", text_font = ("Oswald", 10), command = lambda: self.searchRecords(self.SearchEntry.get()))
        self.SearchButton.grid(column = 1, row = 1, padx = 10, pady = (0, 10))

        self.CreateButton = customtkinter.CTkButton(self.InterFrame, text = "New Patient", text_font = ("Oswald", 10), command = lambda: self.patientEntry())
        self.CreateButton.grid(column = 2, row = 1, padx = 10, pady = (0, 10))

        self.InterFrame.pack(padx = 20, pady = 20) 

        self.TitleFrame.pack(pady = 75)

        self.ResultsFrame = customtkinter.CTkFrame(root, width = 500, height = 500, fg_color = "#6495ED")

        self.ResultInterFrame = customtkinter.CTkFrame(self.ResultsFrame, width = 560, height = 560)

        self.ResultInterFrame.pack(pady = 20, padx = 20)

        self.ResultsFrame.pack(pady = 75)

################################  BREATH ANALYSIS ###############################################
    def breathAnalyze(self, unique):

        for i in self.root.winfo_children():
            i.destroy()


        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        ######### TITLE FRAME #################
        self.TitleFrame = customtkinter.CTkFrame(self.root, width = 50, height = 50, fg_color = "#F0FFFF")

        self.TitleLabel = customtkinter.CTkLabel(self.TitleFrame, text = "BREATH ANALYSIS", text_color = "black")
        self.TitleLabel.configure(font = ("Oswald", 15))
        self.TitleLabel.grid(column = 0, row = 0, rowspan = 3, pady = (10, 10), ipadx = 5, ipady = 5)

        self.TitleFrame.pack(padx = 100, pady = 10)


        ######## INFO FRAME ##################

        self.InfoFrame = customtkinter.CTkFrame(self.root, width = 450, height = 750, fg_color= "#F0FFFF")
        self.conn = sqlite3.connect("records.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("SELECT * FROM patient_list WHERE uniqueid = ?", (unique,))
        item = self.cursor.fetchall()[0]


        self.patientNo = customtkinter.CTkLabel(self.InfoFrame, text = "Patient No: " + item[0], text_color = "black")
        self.patientNo.configure(font = ("Oswald", 10))
        self.patientNo.grid(row = 0, column = 1, pady = 10, padx = 10)

        self.patientName = customtkinter.CTkLabel(self.InfoFrame, text = item[1], text_color = "black")
        self.patientName.configure(font = ("Oswald", 20))
        self.patientName.grid(row = 1, column = 0, columnspan = 2,  pady = 10)

        self.Age = customtkinter.CTkLabel(self.InfoFrame, text = str(2022 - item[-1]) + " years", text_color = "black")
        self.Age.configure(font = ("Oswald", 10))
        self.Age.grid(row = 1, column = 2, pady = 10, padx = 10)

        self.Gender = customtkinter.CTkLabel(self.InfoFrame, text = item[5], text_color = "black")
        self.Gender.configure(font = ("Oswald", 10))
        self.Gender.grid(row = 2, column = 0, pady = 10, padx = 10)

        self.Height = customtkinter.CTkLabel(self.InfoFrame, text = str(item[4]) + "cms", text_color = "black")
        self.Height.configure(font = ("Oswald", 10))
        self.Height.grid(row = 2, column = 1, pady = 10, padx = 10)

        self.Weight = customtkinter.CTkLabel(self.InfoFrame, text = str(item[3]) + "Kgs", text_color = "black")
        self.Weight.configure(font = ("Oswald", 10))
        self.Weight.grid(row = 2, column = 2, pady = 10, padx = 10)


        self.InfoFrame.pack(pady = (50, 100), padx = (10, 10))

        ############ Buttons Frame ####################

        self.ButtonFrame = customtkinter.CTkFrame(self.root, width = 150, height = 400, fg_color = "#F0FFFF")

        self.DeviceLabel = customtkinter.CTkLabel(self.ButtonFrame, text = "Select DrT Device:", text_color = "black")
        self.DeviceLabel.configure(font = ("Oswald", 10))
        self.DeviceLabel.grid(row = 0, column = 0, pady = 20, padx = 20)


        self.DropDown = customtkinter.CTkOptionMenu(self.ButtonFrame, values = ["DR-T-ALPHA01", "DR-T-BETA01"], fg_color = "white", button_color = "#0096FF", text_color = "black")
        self.DropDown.grid(row = 0, column = 1, pady = 20, padx = 40)

        self.SetDeviceLabel = customtkinter.CTkButton(self.ButtonFrame, text = "Set Device", fg_color = "#0096FF", text_font = ("Oswald", 10), text_color = "black")
        self.SetDeviceLabel.grid(row = 0, column = 2, pady = 20, padx = 40)

        self.DurationLabel = customtkinter.CTkLabel(self.ButtonFrame, text = "Duration(Secs):", text_color = "black")
        self.DurationLabel.configure(font = ("Oswald", 10))
        self.DurationLabel.grid(row = 1, column = 0, pady = 20, padx = 40)

        self.TimeDropDown = customtkinter.CTkOptionMenu(self.ButtonFrame, values = ["10", "20", "30"], fg_color = "white", button_color = "#0096FF", text_color = "black")
        self.TimeDropDown.grid(row = 1, column = 1, pady = 20, padx = 40)

        self.ResetDeviceButton = customtkinter.CTkButton(self.ButtonFrame, text = "Reset Device", fg_color = "#0096FF", text_font = ("Oswald", 10), text_color = "black")
        self.ResetDeviceButton.grid(row = 1, column = 2, pady = 20, padx = 40)

        self.NormalImage = PhotoImage(file = "normal.png")
        self.NormalLabel = customtkinter.CTkButton(self.ButtonFrame, text = "Normal", fg_color = "#0096FF", image = self.NormalImage, text_font = ("Oswald", 10), text_color = "black")
        self.NormalLabel.grid(row = 2, column = 0, pady = 20, padx = 40)

        self.MediumImage = PhotoImage(file = "medium.png")
        self.MediumLabel = customtkinter.CTkButton(self.ButtonFrame, text = "Medium", fg_color = "#0096FF", image = self.MediumImage, text_font = ("Oswald", 10), text_color = "black")
        self.MediumLabel.grid(row = 2, column = 1, pady = 20, padx = 40)

        self.HeavyImage = PhotoImage(file = "heavy.png")
        self.HeavyLabel = customtkinter.CTkButton(self.ButtonFrame, text = "Heavy", fg_color = "#0096FF", image = self.HeavyImage, text_font = ("Oswald", 10), text_color = "black")
        self.HeavyLabel.grid(row = 2, column = 2, pady = 20, padx = 40)


        self.ButtonFrame.pack(pady = (0, 50), padx = (10, 10))

        ############################### TIMER FRAME ##################################################

        ############################### Save and Analyze and Back Buttons Frame ######################################
        self.FrameBack = customtkinter.CTkFrame(self.root, width = 200, height = 200, fg_color = "#F0FFFF")

        self.AnalyzeImage = PhotoImage(file = "analyze_save.png")
        self.AnalyzeButton = customtkinter.CTkButton(self.FrameBack, text = "Analyze And Save", text_color = "black", fg_color = "#0096FF", image = self.AnalyzeImage, text_font = ("Oswald", 10), command = lambda: self.analysisReport(unique))
        self.AnalyzeButton.grid(row = 0, column = 0, padx = 10, ipadx = 5, ipady = 5)

        self.BackImage = PhotoImage(file = "back_arrow.png")
        self.BackButton = customtkinter.CTkButton(self.FrameBack, text = "Back To Search", text_color = "black", fg_color = "#0096FF", image = self.BackImage, text_font = ("Oswald", 10), command = self.searchPage)
        self.BackButton.grid(row = 0, column = 1, padx = 10, ipadx = 5, ipady = 5)

        self.FrameBack.pack(padx = 200)


    def analysisReport(self, unique):

        for i in self.root.winfo_children():
            i.destroy()


        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")


        self.conn = sqlite3.connect("records.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM patient_list")
        self.item = self.cursor.fetchall()[0]
        ########################## First Frame ###############################


        self.frame1 = customtkinter.CTkFrame(self.root, width = 150, height = 200, fg_color = "#F0FFFF")

        self.TitleLabel = customtkinter.CTkLabel(self.frame1, text = "ANALYSIS REPORT", text_color = "black")
        self.TitleLabel.configure(font = ("Oswald", 15))
        self.TitleLabel.grid(column = 0, row = 0, columnspan = 3, padx = 10, pady = 10)

        self.NameLabel = customtkinter.CTkLabel(self.frame1, text = self.item[1], text_color = "black")
        self.NameLabel.configure(font = ("Oswald", 10))
        self.NameLabel.grid(column = 0, row = 1, padx = 10, pady = 10)

        self.AgeLabel = customtkinter.CTkLabel(self.frame1, text = str(2022 - self.item[-1]) + " years", text_color = "black")
        self.AgeLabel.configure(font = ("Oswald", 10))
        self.AgeLabel.grid(column = 1, row = 1, padx = 10, pady = 10)

        self.IDLabel = customtkinter.CTkLabel(self.frame1, text = "PID: " + self.item[0], text_color = "black")
        self.IDLabel.configure(font = ("Oswald", 10))
        self.IDLabel.grid(column = 2, row = 1, padx = 10, pady = 10)

        self.WeightLabel = customtkinter.CTkLabel(self.frame1, text = str(self.item[3]) + " Kg", text_color = "black")
        self.WeightLabel.configure(font = ("Oswald", 10))
        self.WeightLabel.grid(column = 0, row = 2, padx = 10, pady = 10)

        self.HeightLabel = customtkinter.CTkLabel(self.frame1, text = str(self.item[4]) + "cm", text_color = "black")
        self.HeightLabel.configure(font = ("Oswald", 10))
        self.HeightLabel.grid(column = 1, row = 2, padx = 10, pady = 10)

        self.GenderLabel = customtkinter.CTkLabel(self.frame1, text = self.item[5], text_color = "black")
        self.GenderLabel.configure(font = ("Oswald", 10))
        self.GenderLabel.grid(column = 2, row = 2, padx = 10, pady = 10)


        self.frame1.pack(padx = 10, pady = 10)

        ################ FRAME 2 ####################################

        # img = Image.open('plot1.png')
        # wpercent = (basewidth / float(img.size[0]))
        # hsize = int((float(img.size[1]) * float(wpercent)))
        # img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        # img.save('resized_plot1.png')

        self.frame2 = customtkinter.CTkFrame(root, width = 600, height = 600, fg_color = "#F0FFFF")

        self.filename = ImageTk.PhotoImage(file = "resized_plot1.png")
        self.background_label = Label(self.frame2, image = self.filename)

        self.background_label.grid(row = 0, column = 0)

        self.frame2.pack(pady = 25, padx = 10)

        ############ FRAME 3 ########################################

        self.wid = 300
        self.hei = 100
        self.frame3 = customtkinter.CTkFrame(root, width = 3 * self.wid, height = 2 * self.hei, fg_color = "#F0FFFF")

        self.RespiratoryFrame = customtkinter.CTkFrame(self.frame3, width = self.wid, height = self.hei, fg_color = "#F0FFFF")

        self.TitleLabel = customtkinter.CTkLabel(self.RespiratoryFrame, text = "50 cycles/min", text_color = "black")
        self.TitleLabel.configure(font = ("Oswald", 14))
        self.TitleLabel.grid(column = 0, row = 0, padx = 10, pady = 10)

        self.CaptionLabel = customtkinter.CTkLabel(self.RespiratoryFrame, text = "Respiration Rate", text_color = "grey")
        self.CaptionLabel.configure(font = ("Oswald", 8))
        self.CaptionLabel.grid(column = 0, row = 1, padx = 10)

        self.RespiratoryFrame.grid(column = 0, row = 0, padx = 40)

        self.RespiratoryFrame = customtkinter.CTkFrame(self.frame3, width = self.wid, height = self.hei, fg_color = "#F0FFFF")

        self.TitleLabel = customtkinter.CTkLabel(self.RespiratoryFrame, text = "50 m/sec", text_color = "black")
        self.TitleLabel.configure(font = ("Oswald", 14))
        self.TitleLabel.grid(column = 0, row = 0, padx = 10, pady = 10)

        self.CaptionLabel = customtkinter.CTkLabel(self.RespiratoryFrame, text = "Mean Inspiration Velocity", text_color = "grey")
        self.CaptionLabel.configure(font = ("Oswald", 8))
        self.CaptionLabel.grid(column = 0, row = 1, padx = 10)

        self.RespiratoryFrame.grid(column = 1, row = 0, padx = 40)

        self.RespiratoryFrame = customtkinter.CTkFrame(self.frame3, width = self.wid, height = self.hei, fg_color = "#F0FFFF")

        self.TitleLabel = customtkinter.CTkLabel(self.RespiratoryFrame, text = "50 m/sec", text_color = "black")
        self.TitleLabel.configure(font = ("Oswald", 14))
        self.TitleLabel.grid(column = 0, row = 0, padx = 10, pady = 10)

        self.CaptionLabel = customtkinter.CTkLabel(self.RespiratoryFrame, text = "Mean Expiration Velocity", text_color = "grey")
        self.CaptionLabel.configure(font = ("Oswald", 8))
        self.CaptionLabel.grid(column = 0, row = 1, padx = 10)

        self.RespiratoryFrame.grid(column = 2, row = 0, padx = 40)

        self.RespiratoryFrame = customtkinter.CTkFrame(self.frame3, width = self.wid, height = self.hei, fg_color = "#F0FFFF")

        self.TitleLabel = customtkinter.CTkLabel(self.RespiratoryFrame, text = "50 Liters/sec", text_color = "black")
        self.TitleLabel.configure(font = ("Oswald", 14))
        self.TitleLabel.grid(column = 0, row = 0, padx = 10, pady = 10)

        self.CaptionLabel = customtkinter.CTkLabel(self.RespiratoryFrame, text = "Mean Inspiration Volume", text_color = "grey")
        self.CaptionLabel.configure(font = ("Oswald", 8))
        self.CaptionLabel.grid(column = 0, row = 1, padx = 10)

        self.RespiratoryFrame.grid(column = 0, row = 1, padx = 40)

        self.RespiratoryFrame = customtkinter.CTkFrame(self.frame3, width = self.wid, height = self.hei, fg_color = "#F0FFFF")

        self.TitleLabel = customtkinter.CTkLabel(self.RespiratoryFrame, text = "50 Liters/sec", text_color = "black")
        self.TitleLabel.configure(font = ("Oswald", 14))
        self.TitleLabel.grid(column = 0, row = 0, padx = 10, pady = 10)

        self.CaptionLabel = customtkinter.CTkLabel(self.RespiratoryFrame, text = "Mean Expiration Volume", text_color = "grey")
        self.CaptionLabel.configure(font = ("Oswald", 8))
        self.CaptionLabel.grid(column = 0, row = 1, padx = 10)

        self.RespiratoryFrame.grid(column = 1, row = 1, padx = 40)

        self.RespiratoryFrame = customtkinter.CTkFrame(self.frame3, width = self.wid, height = self.hei, fg_color = "#F0FFFF")

        self.TitleLabel = customtkinter.CTkLabel(self.RespiratoryFrame, text = "50 Liters/sec", text_color = "black")
        self.TitleLabel.configure(font = ("Oswald", 14))
        self.TitleLabel.grid(column = 0, row = 0, padx = 10, pady = 10)

        self.CaptionLabel = customtkinter.CTkLabel(self.RespiratoryFrame, text = "Mean Tidal Volume", text_color = "grey")
        self.CaptionLabel.configure(font = ("Oswald", 8))
        self.CaptionLabel.grid(column = 0, row = 1, padx = 10)

        self.RespiratoryFrame.grid(column = 2, row = 1, padx = 40)


        self.frame3.pack(pady = 25, padx = 10)

        self.FrameBack = customtkinter.CTkFrame(root, width = 150, height = 150, fg_color = "#0096FF") 

        self.BackButton = customtkinter.CTkButton(self.FrameBack, text = "Back To Search", fg_color = "#0096FF", text_font = ("Oswald", 10), command = lambda: self.breathAnalyze(unique))
        self.BackButton.grid(row = 0, column = 0, padx = 10, ipadx = 5, ipady = 5)

        self.FrameBack.pack()



root = Tk()
App(root)
root.mainloop()



