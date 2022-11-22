from tkinter import *
from turtle import bgcolor, bgpic
from tkinter import ttk 
import tkinter.messagebox
import customtkinter
from PIL import *
import sqlite3
from re import fullmatch
from re import compile
from re import match
from uniqueid import *
import smtplib, ssl
from random import randint




class App:
    def __init__(self, root):
        self.otpgen = 0
        self.valueMonth = [str(i) for i in range(1, 13)]
        self.valueDays = [str(i) for i in range(1, 32)]
        self.valueYears = [str(i) for i in range(1970, 2022)]
        self.root = root
        self.root.title("Doctor T")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.radio_var = IntVar()
        self.loginPage()
        # Create a main frame


    def loginPage(self):
        for i in self.root.winfo_children():
            i.destroy()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.main_frame = customtkinter.CTkFrame(self.root, bg_color = "#2a2d2e", fg_color = "#2a2d2e")
        self.main_frame.pack(fill = BOTH, expand = 1)

        # Create a canvas
        self.my_canvas = Canvas(self.main_frame, bg = "#2a2d2e", scrollregion = (0,0,2000,3200))
        self.my_canvas.pack(side = LEFT, fill = BOTH, expand = 1)

        # Create a scrollbar
        self.myScrollBar = ttk.Scrollbar(self.main_frame, orient = VERTICAL, command = self.my_canvas.yview)
        # self.myScrollBar = customtkinter.CTkScrollbar(self.main_frame, orientation="vertical", command=self.my_canvas.yview, width=20, height = 50, corner_radius=10)
        self.myScrollBar.pack(side = RIGHT, fill = Y)

        # Configure Canvas
        self.my_canvas.configure(yscrollcommand = self.myScrollBar, bg = "#2a2d2e", highlightthickness = 0)
        # self.my_canvas.bind_all("<MouseWheel>", lambda e: self.my_canvas.yview_scroll(-1 * int((e.delta / 120)), "units"))
        self.my_canvas.bind_all("<Configure>", lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Create Another Frame ins
        # \ide the canvas
        self.secondFrame = customtkinter.CTkFrame(self.my_canvas)
        self.my_canvas.create_window((0, 0), window = self.secondFrame, anchor ="nw")

        self.LoginFrame = customtkinter.CTkFrame(self.secondFrame, width = 750, height = 750)


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
        self.Button1 = customtkinter.CTkButton(self.LoginFrame, text = "Log In")
        self.Button1.grid(row = 5, column = 0, pady = (50, 40), padx = (150, 0), sticky = NE)

        # Register Button
        self.Button2 = customtkinter.CTkButton(self.LoginFrame, text = "Register", command = lambda: self.registerPatient(self.root))
        self.Button2.grid(row = 5, column = 1, pady = (50, 40))

        self.LoginFrame.grid(row = 2, column = 0, pady = 100, padx = (400, 0))
        # self.root.eval('tk::PlaceWindow . center')
        

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



    def registerPatient(self, root):
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
        # self.my_canvas.bind_all("<MouseWheel>", lambda e: self.my_canvas.yview_scroll(-1 * int((e.delta / 120)), "units"))
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
 


root = customtkinter.CTk()
App(root)
root.eval("tk::PlaceWindow . center")
root.mainloop()
