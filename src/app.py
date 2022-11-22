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
import smtplib, ssl
from uniqueid import *




class App:
    def __init__(self, root):
        self.root = root
        self.otpgen = 0
        self.root.title("Doctor T")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.radio_var = IntVar()
        self.valueMonth = [str(i) for i in range(1, 13)]
        self.valueDays = [str(i) for i in range(1, 32)]
        self.valueYears = [str(i) for i in range(1970, 2022)]
        self.loginPage()
        # Create a main frame


    def removeLabel(self, Label):
        Label.grid_remove()
 
    def showLabel(self, Label, x, y):
        Label.grid(column = y, row = x, pady = (50, 0), padx = (20, 0))

    def otpMessage(self, reciever):

        self.otpgen = randint(100000, 999999)

        port = 465
        password = "hpykhkzwafrrupny"
        email = "doctortdonotreply@gmail.com"
        message = "Your OTP for email ID verification is " + str(self.otpgen) + ". Please enter this OTP where prompted."

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
            server.login(email, password)
            server.sendmail(email, reciever, message)


    def successfulMessage(self, reciever, uniqueid):
        message = "Dear User, Your Unique ID for Doctor T Registration is " + uniqueid + "." + " Please save this information for future reference."
        port = 465
        password = "fbqzdsujolwqhutv"
        email = "doctortdonotreply@gmail.com"

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
            server.login(email, password)
            server.sendmail(email, reciever, message)


    def verifyOTP(self):
        entered = int(self.otp.get())
        gen = int(self.otpgen)
        if gen == entered:
            self.pastesLabel = customtkinter.CTkLabel(self.secondFrame, text = "OTP verified successfully", text_color = "green")
            self.pastesLabel.grid(row = 9, column = 18, columnspan = 2, pady = (50, 0), padx = (20, 0))
        else:
            self.pastefLabel = customtkinter.CTkLabel(self.secondFrame, text = "Incorrect OTP!", text_color = "red")
            self.pastefLabel.grid(row = 9, column = 18, columnspan = 2, pady = (50, 0), padx = (20, 0))

    ################################ Checking User Info ######################################

    def loginUser(self):
        flag = 0
        conn = sqlite3.connect("records.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM account")
        user = self.username.get()
        pwd = self.password.get()
        print(user, pwd)
        accounts = cursor.fetchall()
        for account in accounts:
            flag = 0
            if user in account:
                flag = 1
                if pwd == account[1]:
                    print(account[0], account[1])
                    self.searchPage()
                    break          
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

    ################################### Creating Patient Record ###########################################

    def patientEntry(self):
        self.gender1 = ""
        self.flag = 0
        self.fname1 = self.first.get()
        self.mname1 = self.middle.get()
        self.lname1 = self.last.get()
        self.day1 = int(self.day.get()) 
        self.month1 = int(self.month.get())
        self.year1 = int(self.year.get())
        self.email1 = self.email.get()


        self.emailRegex = compile("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
        if fullmatch(self.emailRegex, self.email.get()):
            self.email1 = self.email.get()
            self.removeLabel(self.EmailErrorLabel)
        else:
            self.showLabel(self.EmailErrorLabel, 9, 18)      #row = 9, column = 18
            self.flag = 1


        self.phoneRegex = compile("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")
        if fullmatch(self.phoneRegex, self.phone.get()):
            self.phone1 = self.phone.get()
            self.removeLabel(self.PhoneErrorLabel)
        else:
            self.showLabel(self.PhoneErrorLabel, 5, 10)   # Phone Show row = 5, column = 10
            self.flag = 1
    
        self.weightRegex = compile("^([0-9]{2,3})")
        if fullmatch(self.weightRegex, self.weight.get()):
            self.weight1 = self.weight.get()
            self.removeLabel(self.WeightErrorLabel)
        else:
            self.showLabel(self.WeightErrorLabel, 7, 10) # Weight SHOW column = 10, row = 7
            self.flag = 1

        self.uidaiRegex = compile("^[2-9]{1}[0-9]{11}$")
        if fullmatch(self.uidaiRegex, self.uidai.get()):
            self.uniqueid = "P" + str(self.uidai.get())
            self.removeLabel(self.UidaiErrorLabel)
        else:
            self.showLabel(self.UidaiErrorLabel, 6, 10)  # row = 6, column = 10
            self.flag = 1


        self.heightRegex = compile("^([0-9]{2,3})")
        if fullmatch(self.heightRegex, self.height.get()):
            self.height1 = self.height.get()
            self.removeLabel(self.HeightErrorLabel)
        else:
            self.showLabel(self.HeightErrorLabel, 8, 10)# row = 8, column = 10 
            self.flag = 1

        if self.radio_var.get() == 1:
            self.gender1 = self.gender1 + "Male"
            self.removeLabel(self.GenderErrorLabel)
        elif self.radio_var.get() == 2:
            self.gender1 = self.gender1 + "Female"
            self.removeLabel(self.GenderErrorLabel)
        elif self.radio_var.get() == 3:
            self.gender1 = self.gender1 + "Non-Binary"
            self.removeLabel(self.GenderErrorLabel)
        else: 
            self.flag == 1
            self.showLabel(self.GenderErrorLabel, 4, 12)
    
        if self.flag == 0:
            self.conn = sqlite3.connect("records.db")
            self.cursor = self.conn.cursor()
            print(self.radio_var, self.uniqueid, self.email1, self.fname1, self.mname1, self.lname1, int(self.phone1), int(self.weight1), int(self.height1), self.gender1, int(self.day1), int(self.month1), int(self.year1))
            self.cursor.execute("INSERT INTO patient_list VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.uniqueid, self.email1, self.fname1, self.mname1, self.lname1, int(self.phone1), int(self.weight1), int(self.height1), self.gender1, int(self.day1), int(self.month1), int(self.year1)))
            self.conn.commit()
            self.conn.close()
            tkinter.messagebox.showinfo("Successful", "Account Created Successfully")
            self.successfulMessage(self.email1, self.uniqueid)
            self.first.delete(0, END)
            self.last.delete(0, END)
            self.middle.delete(0, END)
            self.phone.delete(0, END)
            self.uidai.delete(0, END)
            self.weight.delete(0, END)
            self.height.delete(0, END)
            self.email.delete(0, END)
            self.otp.delete(0, END)
            self.day.set("1")
            self.month.set("1")
            self.year.set("1970")
            self.radio_var.set(0)
   
    ################################## Search Page Database ######################################################

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

            NameLabel = customtkinter.CTkLabel(self.ResultInterFrame, text = item[2] + " " + item [4])
            NameLabel.configure(font = ("Oswald", 10))
            NameLabel.grid(row = index, column = 1, pady = 10, padx = 10)

            ViewButton = customtkinter.CTkButton(self.ResultInterFrame, text = "View", text_font = ("Oswald", 10), command = lambda: self.breathAnalyze(item[0]))
            ViewButton.grid(row = index, column = 2, pady = 10, padx = 10)
            index += 1
        if len(self.searchResults) == 0:
            NotFoundLabel = customtkinter.CTkLabel(self.ResultInterFrame, text = "No records found!!")
            NotFoundLabel.configure(font = ("Oswald", 15))
            NotFoundLabel.grid(row = 0, column = 0, columnspan = 3, padx = 200, pady = 50)


    ######################################## Login Page ###################################################

    def loginPage(self):
        for i in self.root.winfo_children():
            i.destroy()



        self.LoginFrame = customtkinter.CTkFrame(self.root, width = 750, height = 750)


        # Title Label
        self.TitleLabel = customtkinter.CTkLabel(self.LoginFrame, text = "Doctor T", text_color = "#0096FF")
        self.TitleLabel.configure(font = ("Pacifico", 25))
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

        self.LoginFrame.grid(row = 2, column = 0, pady = 100, padx = (400, 0))
        # self.root.eval('tk::PlaceWindow . center')

    ##################### NEW USER REGISTRATION PAGE ##################################

    def registerPage(self):
        for i in self.root.winfo_children():
            i.destroy()
        
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.frame = customtkinter.CTkFrame(self.root, width = 750, height = 750)


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

        self.frame.grid(row = 2, column = 0, pady = 100, padx = (550, 0))
        # root.eval('tk::PlaceWindow . center')


################################ Patient Data Entry Page #############################################
    
    def registerPatient(self):
        for i in self.root.winfo_children():
            i.destroy()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.main_frame = customtkinter.CTkFrame(self.root, bg_color = "#2a2d2e", fg_color = "#2a2d2e")
        self.main_frame.pack(fill = BOTH, expand = 1)

        # Create a canvas
        self.my_canvas = Canvas(self.main_frame, bg = "#2a2d2e")
        self.my_canvas.pack(side = LEFT, fill = BOTH, expand = 1)

        # Create a scrollbar
        self.myScrollBar = ttk.Scrollbar(self.main_frame, orient = VERTICAL, command = self.my_canvas.yview)
        # self.myScrollBar = customtkinter.CTkScrollbar(self.main_frame, orientation="vertical", command=self.my_canvas.yview, width=20, height = 50, corner_radius=10)
        self.myScrollBar.pack(side = RIGHT, fill = Y)

        # Configure Canvas
        self.my_canvas.configure(yscrollcommand = self.myScrollBar, bg = "#2a2d2e", highlightthickness = 0)
        # self.my_canvas.bind_all("<Configure>", lambda e: self.my_canvas.yview_scroll(-1 * int((e.delta / 120)), "units"))
        self.my_canvas.bind_all("<Configure>", lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Create Another Frame ins
        # \ide the canvas
        self.secondFrame = customtkinter.CTkFrame(self.my_canvas)
        self.my_canvas.create_window((0, 0), window = self.secondFrame, anchor ="nw")

    
        self.radio_var = IntVar()
        self.check_var = IntVar()

        self.LabelTest = customtkinter.CTkLabel(self.secondFrame, text = "Registration Form", text_color = "#EE4B2B")
        self.LabelTest.configure(font = ("Pacifico", 25))
        self.LabelTest.grid(row = 0, column = 8, columnspan = 10, pady = (0, 0))

        font1 = "Oswald"

        self.caption = customtkinter.CTkLabel(self.secondFrame, text = "Enter your name:")
        self.caption.configure(font = (font1, 12))
        self.caption.grid(row = 2, column = 0, padx = (50, 50), columnspan = 6)

        self.firstLabel = customtkinter.CTkLabel(self.secondFrame, text = "First Name")
        self.firstLabel.configure(font = (font1, 10))
        self.firstLabel.grid(row = 1, column = 6, padx = 50, columnspan = 4, pady = (50, 0))

        self.middleLabel = customtkinter.CTkLabel(self.secondFrame, text = "Middle Name")
        self.middleLabel.configure(font = (font1, 10))
        self.middleLabel.grid(row = 1, column = 10, padx = 50, columnspan = 4, pady = (50, 0))

        self.lastLabel = customtkinter.CTkLabel(self.secondFrame, text = "Last Name")
        self.lastLabel.configure(font = (font1, 10))
        self.lastLabel.grid(row = 1, column = 14, padx = 50, columnspan = 4, pady = (50, 0))

        self.first = customtkinter.CTkEntry(self.secondFrame, placeholder_text = "Enter First Name", width = 200)
        self.first.grid(row = 2, column = 6, columnspan = 4, padx = 50)

        self.middle = customtkinter.CTkEntry(self.secondFrame, placeholder_text = "Enter Middle Name", width = 200)
        self.middle.grid(row = 2, column = 10, columnspan = 4, padx = 50)

        self.last = customtkinter.CTkEntry(self.secondFrame, placeholder_text = "Enter Last Name", width = 200)
        self.last.grid(row = 2, column = 14, columnspan = 4, padx = 50)

        self.dayLabel = customtkinter.CTkLabel(self.secondFrame, text = "Date of birth:")
        self.dayLabel.configure(font = (font1, 12))
        self.dayLabel.grid(row = 3, column = 0, columnspan = 6, pady = (50, 0))

        self.day = customtkinter.CTkOptionMenu(self.secondFrame, values = self.valueDays)
        self.day.grid(row = 3, column = 6, columnspan = 4, pady = (50, 0))

        self.monthLabel = customtkinter.CTkLabel(self.secondFrame, text = "Month:")
        self.monthLabel.configure(font = (font1, 12))
        self.monthLabel.grid(row = 3, column = 10, columnspan = 2, pady = (50, 0))

        self.month = customtkinter.CTkOptionMenu(self.secondFrame, values = self.valueMonth)
        self.month.grid(row = 3, column = 12, columnspan = 2, pady = (50, 0))

        self.yearLabel = customtkinter.CTkLabel(self.secondFrame, text = "Year:")
        self.yearLabel.configure(font = (font1, 12))
        self.yearLabel.grid(row = 3, column = 14, columnspan = 2, pady = (50, 0))

        self.year = customtkinter.CTkOptionMenu(self.secondFrame, values = self.valueYears)
        self.year.grid(row = 3, column = 16, columnspan = 2, pady = (50, 0))

        self.Gender = customtkinter.CTkLabel(self.secondFrame, text = "Gender:")
        self.Gender.configure(font = (font1, 12))
        self.Gender.grid(row = 4, column = 0, padx = (50, 50), columnspan = 6, pady = (50, 0))

        self.male = customtkinter.CTkRadioButton(self.secondFrame, text = "Male", variable = self.radio_var, value = 1)
        self.male.configure(text_font = (font1, 10))
        self.male.grid(column = 6, row = 4, columnspan = 2, pady = (50, 0))

        self.female = customtkinter.CTkRadioButton(self.secondFrame, text = "Female", variable = self.radio_var, value = 2)
        self.female.configure(text_font = (font1, 10))
        self.female.grid(column = 8, row = 4, columnspan = 2, pady = (50, 0))

        self.nonbinary = customtkinter.CTkRadioButton(self.secondFrame, text = "Non-Binary", variable = self.radio_var, value = 3)
        self.nonbinary.configure(text_font = (font1, 10))
        self.nonbinary.grid(column = 10, row = 4, columnspan = 2, pady = (50, 0))

        self.phoneLabel = customtkinter.CTkLabel(self.secondFrame, text = "Phone Number:")
        self.phoneLabel.configure(font = (font1, 12))
        self.phoneLabel.grid(row = 5, column = 0, padx = (50, 50), columnspan = 6, pady = (50, 0))

        self.phone = customtkinter.CTkEntry(self.secondFrame, placeholder_text = "Phone Number", width = 200)
        self.phone.grid(row = 5, column = 6, columnspan = 4, pady = (50, 0))

        self.AdhaarLabel = customtkinter.CTkLabel(self.secondFrame, text = "UIDAI Number:")
        self.AdhaarLabel.configure(font = (font1, 12))
        self.AdhaarLabel.grid(row = 6, column = 0, padx = (50, 50), columnspan = 6, pady = (50, 0))

        self.uidai = customtkinter.CTkEntry(self.secondFrame, placeholder_text = "Enter your Adhaar Number", width = 200)
        self.uidai.grid(row = 6, column = 6, columnspan = 4, pady = (50, 0))

        self.weightLabel = customtkinter.CTkLabel(self.secondFrame, text = "Weight:")
        self.weightLabel.configure(font = (font1, 12))
        self.weightLabel.grid(row = 7, column = 0, padx = (50, 50), columnspan = 6, pady = (50, 0))

        self.weight = customtkinter.CTkEntry(self.secondFrame, placeholder_text = "Weight in kgs.", width = 200)
        self.weight.grid(row = 7, column = 6, columnspan = 4, pady = (50, 0))

        self.heightLabel = customtkinter.CTkLabel(self.secondFrame, text = "Height:")
        self.heightLabel.configure(font = (font1, 12))
        self.heightLabel.grid(row = 8, column = 0, padx = (50, 50), columnspan = 4, pady = (50, 0))

        self.height = customtkinter.CTkEntry(self.secondFrame, placeholder_text = "Height in cms.", width = 200)
        self.height.grid(row = 8, column = 6, columnspan = 4, pady = (50, 0))

        self.emailLabel = customtkinter.CTkLabel(self.secondFrame, text = "Email:")
        self.emailLabel.configure(font = (font1, 12))
        self.emailLabel.grid(row = 9, column = 0, padx = (50, 50), columnspan = 6, pady = (50, 0))

        self.email = customtkinter.CTkEntry(self.secondFrame, placeholder_text = "Enter valid email id.", width = 200)
        self.email.grid(row = 9, column = 6, columnspan = 4, pady = (50, 0))

        self.sendOTPButton = customtkinter.CTkButton(self.secondFrame, text = "Send OTP", text_font = (font1, 10), command = lambda: self.otpMessage(self.email.get()))
        self.sendOTPButton.grid(row = 9, column = 10, columnspan = 2, pady = (50, 0))

        self.OTPLabel = customtkinter.CTkLabel(self.secondFrame, text = "OTP:")
        self.OTPLabel.configure(font = (font1, 12))
        self.OTPLabel.grid(row = 9, column = 12, columnspan = 2, pady = (50, 0))

        self.otp = customtkinter.CTkEntry(self.secondFrame, placeholder_text = "Enter OTP recieved.", width = 200)
        self.otp.grid(row = 9, column = 14, columnspan = 2, pady = (50, 0), padx = (0, 25))

        self.verifyOTPButton = customtkinter.CTkButton(self.secondFrame, text = "Verify OTP", text_font = (font1, 10), command = self.verifyOTP)
        self.verifyOTPButton.grid(row = 9, column = 16, columnspan = 2, pady = (50, 0))

        self.checkbox = customtkinter.CTkCheckBox(self.secondFrame, text="", variable=self.check_var, onvalue="on", offvalue="off")
        self.checkbox.grid(row = 10, column = 0, pady = (100, 0), padx = (50, 50), columnspan = 6)

        self.CheckBoxLabel = customtkinter.CTkLabel(self.secondFrame, text = "CATS does not claim any responsibility for any damages incurred. Check the box if you agree to this condition.", text_color = "grey")
        self.CheckBoxLabel.grid(row = 10, column = 6, pady = (100, 0), columnspan = 10)

        self.CreateButton = customtkinter.CTkButton(self.secondFrame, text = "Create Record", text_font = (font1, 10), command = self.patientEntry)
        self.CreateButton.grid(column = 10, row = 12, pady = (25, 0))

        self.BackButton = customtkinter.CTkButton(self.secondFrame, text = "Search Records", text_font = (font1, 10), command = lambda: self.searchPage())
        self.BackButton.grid(column = 14, row = 12, pady = (25, 0))       

        self.EmailErrorLabel = customtkinter.CTkLabel(self.secondFrame, text = "Invalid Email Address. Please Check.", bg_color = "#FF3131")
        self.PhoneErrorLabel = customtkinter.CTkLabel(self.secondFrame, text = "Invalid Phone Number. Please Check.", bg_color = "#FF3131")
        self.WeightErrorLabel = customtkinter.CTkLabel(self.secondFrame, text = "Invalid Weight", bg_color = "#FF3131")
        self.UidaiErrorLabel = customtkinter.CTkLabel(self.secondFrame, text = "Invalid Adhaar. Please Check.", bg_color = "#FF3131")
        self.HeightErrorLabel = customtkinter.CTkLabel(self.secondFrame, text = "Invalid Height.", bg_color = "#FF3131")
        self.GenderErrorLabel = customtkinter.CTkLabel(self.secondFrame, text = "Please pick the gender you identify with.", bg_color = "#FF3131")
 

   

    ################################  BREATH ANALYSIS ###############################################

    def breathAnalyze(self, unique):

        for i in self.root.winfo_children():
            i.destroy()


        self.main_frame = customtkinter.CTkFrame(self.root, bg_color = "#2a2d2e", fg_color = "#2a2d2e")
        self.main_frame.pack(fill = BOTH, expand = 1)

        # Create a canvas
        self.my_canvas = Canvas(self.main_frame, bg = "#2a2d2e")
        self.my_canvas.pack(side = LEFT, fill = BOTH, expand = 1)

        # Create a scrollbar
        self.myScrollBar = ttk.Scrollbar(self.main_frame, orient = VERTICAL, command = self.my_canvas.yview)
        # self.myScrollBar = customtkinter.CTkScrollbar(self.main_frame, orientation="vertical", command=self.my_canvas.yview, width=20, height = 50, corner_radius=10)
        self.myScrollBar.pack(side = RIGHT, fill = Y)

        # Configure Canvas
        self.my_canvas.configure(yscrollcommand = self.myScrollBar, bg = "#2a2d2e", highlightthickness = 0)
        # self.my_canvas.bind_all("<Configure>", lambda e: self.my_canvas.yview_scroll(-1 * int((e.delta / 120)), "units"))
        self.my_canvas.bind_all("<Configure>", lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Create Another Frame ins
        # Hide the canvas
        self.secondFrame = customtkinter.CTkFrame(self.my_canvas)
        self.my_canvas.create_window((0, 0), window = self.secondFrame, anchor ="nw")

        ########################### TITLE FRAME #######################################################

        self.TitleFrame = customtkinter.CTkFrame(self.secondFrame, width = 50, height = 50, fg_color = "#212325")

        self.TitleLabel = customtkinter.CTkLabel(self.TitleFrame, text = "BREATH ANALYSIS")
        self.TitleLabel.configure(font = ("Oswald", 15))
        self.TitleLabel.grid(column = 0, row = 0, rowspan = 3, pady = (10, 10), ipadx = 5, ipady = 5)

        self.TitleFrame.pack(padx = 100, pady = 10)


        ########################## INFO FRAME #########################################################

        self.InfoFrame = customtkinter.CTkFrame(self.secondFrame, width = 450, height = 750, fg_color = "#212325")
        self.conn = sqlite3.connect("records.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("SELECT * FROM patient_list WHERE uniqueid = ?", (unique,))
        item = self.cursor.fetchall()[0]


        self.patientNo = customtkinter.CTkLabel(self.InfoFrame, text = "Patient No: " + item[0])
        self.patientNo.configure(font = ("Oswald", 10))
        self.patientNo.grid(row = 0, column = 1, pady = 10, padx = 10)

        self.patientName = customtkinter.CTkLabel(self.InfoFrame, text = item[2])
        self.patientName.configure(font = ("Oswald", 20))
        self.patientName.grid(row = 1, column = 0, columnspan = 2,  pady = 10)

        self.Age = customtkinter.CTkLabel(self.InfoFrame, text = str(2022 - item[-1]) + " years")
        self.Age.configure(font = ("Oswald", 10))
        self.Age.grid(row = 1, column = 2, pady = 10, padx = 10)

        self.Gender = customtkinter.CTkLabel(self.InfoFrame, text = item[8])
        self.Gender.configure(font = ("Oswald", 10))
        self.Gender.grid(row = 2, column = 0, pady = 10, padx = 10)

        self.Height = customtkinter.CTkLabel(self.InfoFrame, text = str(item[7]) + "cms")
        self.Height.configure(font = ("Oswald", 10))
        self.Height.grid(row = 2, column = 1, pady = 10, padx = 10)

        self.Weight = customtkinter.CTkLabel(self.InfoFrame, text = str(item[6]) + "Kgs")
        self.Weight.configure(font = ("Oswald", 10))
        self.Weight.grid(row = 2, column = 2, pady = 10, padx = 10)


        self.InfoFrame.pack(pady = (50, 100), padx = (10, 10))

        ############ Buttons Frame ####################

        self.ButtonFrame = customtkinter.CTkFrame(self.secondFrame, width = 150, height = 400, fg_color = "#212325")

        self.DeviceLabel = customtkinter.CTkLabel(self.ButtonFrame, text = "Select DrT Device:")
        self.DeviceLabel.configure(font = ("Oswald", 10))
        self.DeviceLabel.grid(row = 0, column = 0, pady = 20, padx = 20)


        self.DropDown = customtkinter.CTkOptionMenu(self.ButtonFrame, values = ["DR-T-ALPHA01", "DR-T-BETA01"], button_color = "#0096FF")
        self.DropDown.grid(row = 0, column = 1, pady = 20, padx = 40)

        self.SetDeviceLabel = customtkinter.CTkButton(self.ButtonFrame, text = "Set Device", fg_color = "#0096FF", text_font = ("Oswald", 10))
        self.SetDeviceLabel.grid(row = 0, column = 2, pady = 20, padx = 40)

        self.DurationLabel = customtkinter.CTkLabel(self.ButtonFrame, text = "Duration(Secs):")
        self.DurationLabel.configure(font = ("Oswald", 10))
        self.DurationLabel.grid(row = 1, column = 0, pady = 20, padx = 40)

        self.TimeDropDown = customtkinter.CTkOptionMenu(self.ButtonFrame, values = ["10", "20", "30"], button_color = "#0096FF")
        self.TimeDropDown.grid(row = 1, column = 1, pady = 20, padx = 40)

        self.ResetDeviceButton = customtkinter.CTkButton(self.ButtonFrame, text = "Reset Device", fg_color = "#0096FF", text_font = ("Oswald", 10))
        self.ResetDeviceButton.grid(row = 1, column = 2, pady = 20, padx = 40)

        self.NormalImage = PhotoImage(file = "normal.png")
        self.NormalLabel = customtkinter.CTkButton(self.ButtonFrame, text = "Normal", fg_color = "#0096FF", image = self.NormalImage, text_font = ("Oswald", 10))
        self.NormalLabel.grid(row = 2, column = 0, pady = 20, padx = 40)

        self.MediumImage = PhotoImage(file = "medium.png")
        self.MediumLabel = customtkinter.CTkButton(self.ButtonFrame, text = "Medium", fg_color = "#0096FF", image = self.MediumImage, text_font = ("Oswald", 10))
        self.MediumLabel.grid(row = 2, column = 1, pady = 20, padx = 40)

        self.HeavyImage = PhotoImage(file = "heavy.png")
        self.HeavyLabel = customtkinter.CTkButton(self.ButtonFrame, text = "Heavy", fg_color = "#0096FF", image = self.HeavyImage, text_font = ("Oswald", 10))
        self.HeavyLabel.grid(row = 2, column = 2, pady = 20, padx = 40)


        self.ButtonFrame.pack(pady = (0, 50), padx = (10, 10))

        ############################### TIMER FRAME ##################################################

        ############################### Save and Analyze and Back Buttons Frame ######################################
        self.FrameBack = customtkinter.CTkFrame(self.secondFrame, width = 200, height = 200, fg_color = "#212325")

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

        self.my_canvas = Canvas(self.main_frame, bg = "#2a2d2e")

        self.conn = sqlite3.connect("records.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM patient_list")
        self.item = self.cursor.fetchall()[0]
        ########################## First Frame ###############################


        self.frame1 = customtkinter.CTkFrame(self.root, width = 150, height = 200)

        self.TitleLabel = customtkinter.CTkLabel(self.frame1, text = "ANALYSIS REPORT")
        self.TitleLabel.configure(font = ("Oswald", 15))
        self.TitleLabel.grid(column = 0, row = 0, columnspan = 3, padx = 10, pady = 10)

        self.NameLabel = customtkinter.CTkLabel(self.frame1, text = self.item[1])
        self.NameLabel.configure(font = ("Oswald", 10))
        self.NameLabel.grid(column = 0, row = 1, padx = 10, pady = 10)

        self.AgeLabel = customtkinter.CTkLabel(self.frame1, text = str(2022 - self.item[-1]) + " years")
        self.AgeLabel.configure(font = ("Oswald", 10))
        self.AgeLabel.grid(column = 1, row = 1, padx = 10, pady = 10)

        self.IDLabel = customtkinter.CTkLabel(self.frame1, text = "PID: " + self.item[0])
        self.IDLabel.configure(font = ("Oswald", 10))
        self.IDLabel.grid(column = 2, row = 1, padx = 10, pady = 10)

        self.WeightLabel = customtkinter.CTkLabel(self.frame1, text = str(self.item[3]) + " Kg")
        self.WeightLabel.configure(font = ("Oswald", 10))
        self.WeightLabel.grid(column = 0, row = 2, padx = 10, pady = 10)

        self.HeightLabel = customtkinter.CTkLabel(self.frame1, text = str(self.item[4]) + "cm")
        self.HeightLabel.configure(font = ("Oswald", 10))
        self.HeightLabel.grid(column = 1, row = 2, padx = 10, pady = 10)

        self.GenderLabel = customtkinter.CTkLabel(self.frame1, text = self.item[5])
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

        self.filename = ImageTk.PhotoImage(file = "img\\resized_plot1.png")
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


    def searchPage(self):

        for i in self.root.winfo_children():
            i.destroy()


        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.TitleFrame = customtkinter.CTkFrame(self.root, width = 500, height = 500, fg_color = "#6495ED")

        self.InterFrame = customtkinter.CTkFrame(self.TitleFrame, width = 460, height = 460, fg_color = "#0047AB")

        self.TitleLabel = customtkinter.CTkLabel(self.InterFrame, text = "SEARCH PATIENT RECORDS", text_color = "white")
        self.TitleLabel.configure(font = ("Oswald", 15))
        self.TitleLabel.grid(column = 0, row = 0, columnspan = 3, padx = 10, pady = 20)

        self.SearchEntry = customtkinter.CTkEntry(self.InterFrame, placeholder_text = "Search for patients", width = 150)
        self.SearchEntry.grid(column = 0, row = 1, padx = 10, pady = (0, 10))

        self.SearchButton = customtkinter.CTkButton(self.InterFrame, text = "Search", text_font = ("Oswald", 10), command= lambda: self.searchRecords(self.SearchEntry.get()))
        self.SearchButton.grid(column = 1, row = 1, padx = 10, pady = (0, 10))

        self.CreateButton = customtkinter.CTkButton(self.InterFrame, text = "New Patient", text_font = ("Oswald", 10), command = lambda: self.registerPatient())
        self.CreateButton.grid(column = 2, row = 1, padx = 10, pady = (0, 10))

        self.InterFrame.pack(padx = 20, pady = 20) 

        self.TitleFrame.pack(pady = 75)

        self.ResultsFrame = customtkinter.CTkFrame(self.root, width = 500, height = 500, fg_color = "#6495ED")

        self.ResultInterFrame = customtkinter.CTkFrame(self.ResultsFrame, width = 560, height = 560)

        self.ResultInterFrame.pack(pady = 20, padx = 20)

        self.ResultsFrame.pack(pady = 75)





root = customtkinter.CTk()
App(root)
root.eval("tk::PlaceWindow . center")
root.mainloop()



