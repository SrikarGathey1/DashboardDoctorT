from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
from PIL import ImageFont
from turtle import color
import customtkinter
import sqlite3
from uniqueid import *
from re import fullmatch
from re import compile

############### DATABASE CODE BEGINS ##############################

def newPatient():
    flag = 0
    gender1 = "None"
    name1 = name.get()
    height1 = height.get()
    day1 = int(day.get()) 
    month1 = int(month.get())
    year1 = int(year.get())

    unique1 = unique_id_compute(name1, year1)
    
    phoneRegex = compile("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")
    if fullmatch(phoneRegex, phone.get()):
        phone1 = phone.get()
    else:
        ErrorLabel = customtkinter.CTkLabel(frame, text = "Invalid Phone Number", bg_color = "#FF3131")
        ErrorLabel.grid(column = 2, row = 2, pady = (0, 25))
        flag = 1
    
    weightRegex = compile("^([0-9]{2,3})")
    if fullmatch(weightRegex, weight.get()):
        weight1 = weight.get()
    else:
        ErrorLabel = customtkinter.CTkLabel(frame, text = "Invalid Weight", bg_color = "#FF3131")
        ErrorLabel.grid(column = 2, row = 3, pady = (0, 25))
        flag = 1

    heightRegex = compile("^([0-9]{2,3})")
    if fullmatch(heightRegex, height.get()):
        height1 = height.get()
    else:
        ErrorLabel = customtkinter.CTkLabel(frame, text = "Invalid Height", bg_color = "#FF3131")
        ErrorLabel.grid(column = 2, row = 4, pady = (0, 25))
        flag = 1

    if radio_var == 1:
        gender1 = "Male"
    elif radio_var == 2:
        gender1 = "Female"
    elif radio_var == 3:
        gender1 = "Non-Binary"
    
    if flag == 0:
        conn = sqlite3.connect("records.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO patient_list VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (unique1, name1, phone1, weight1, height1, gender1, day1, month1, year1))
        conn.commit()
        conn.close()
        BaseLabel.destroy()
        SuccessLabel = customtkinter.CTkLabel(frame, text = "Unique ID:" + unique1, bg_color = "#FF3131")
        SuccessLabel.grid(row = 9, column = 3)
    return


############### DATABASE CODE ENDS #################################

valueMonth = [str(i) for i in range(1, 13)]
valueDays = [str(i) for i in range(1, 32)]
valueYears = [str(i) for i in range(1970, 2022)]


root = Tk()
root.title("Doctor T: Know Your Breath")
radio_var = IntVar()

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


filename = PhotoImage(file = "smaller.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


frame = customtkinter.CTkFrame(root, width = 1500, height = 2000, bg_color = "white")

FormTitleLabel = customtkinter.CTkLabel(frame, text = "New Patient Form", text_color = "#FF3131")
FormTitleLabel.configure(font = ("Pacifico", 25))
FormTitleLabel.grid(column = 0, columnspan = 6, row = 0, sticky = N, padx = (150, 100), pady = (25, 25))

NameLabel = customtkinter.CTkLabel(frame, text = "Name")
NameLabel.configure(font = ("Helvetica", 12))
NameLabel.grid(column = 0, row = 1, padx = (0, 50), pady = (25, 25))

name = customtkinter.CTkEntry(frame, width = 300, placeholder_text = "Enter Patient Name")
name.grid(column = 4, row = 1, columnspan = 2, padx = (10, 10), pady = (25, 25))

PhoneLabel = customtkinter.CTkLabel(frame, text = "Phone")
PhoneLabel.configure(font = ("Helvetica", 12))
PhoneLabel.grid(column = 0, row = 2, padx = (0, 50), pady = (0, 25))

phone = customtkinter.CTkEntry(frame, width = 300, placeholder_text = "Enter Patient Phone Number")
phone.grid(column = 4, row = 2, columnspan = 2, padx = (10, 10), pady = (0, 25))

WeightLabel = customtkinter.CTkLabel(frame, text = "Weight")
WeightLabel.configure(font = ("Helvetica", 12))
WeightLabel.grid(column = 0, row = 3, padx = (0, 50), pady = (0, 25))

weight = customtkinter.CTkEntry(frame, width = 300, placeholder_text = "Enter Patient Weight In KGs")
weight.grid(column = 4, row = 3, columnspan = 2, padx = (10, 10), pady = (0, 25))

HeightLabel = customtkinter.CTkLabel(frame, text = "Height")
HeightLabel.configure(font = ("Helvetica", 12))
HeightLabel.grid(column = 0, row = 4, padx = (0, 50), pady = (0, 25))

height = customtkinter.CTkEntry(frame, width = 300, placeholder_text = "Enter Patient Height In Cm")
height.grid(column = 4, row = 4, columnspan = 2, padx = (10, 10), pady = (0, 25))


GenderLabel = customtkinter.CTkLabel(frame, text = "Gender")
GenderLabel.configure(font = ("Helvetica", 12))
GenderLabel.grid(column = 0, row = 5, padx = (0, 50), pady = (25, 25))

male = customtkinter.CTkRadioButton(frame, text = "Male", border_color ="#FF3131", fg_color = "#FF3131", variable = radio_var, value = 1)
male.grid(column = 2, row = 5, pady = (25, 25))

female = customtkinter.CTkRadioButton(frame, text = "Female", border_color = "#FF3131", fg_color = "#FF3131", variable = radio_var, value = 2)
female.grid(column = 3, row = 5, pady = (25, 25))

nonbinary = customtkinter.CTkRadioButton(frame, text = "Non-Binary", border_color = "#FF3131", fg_color = "#FF3131", variable = radio_var, value = 3)
nonbinary.grid(column = 4, row = 5, pady = (25, 25), padx = (0, 75))

DayLabel = customtkinter.CTkLabel(frame, text = "Day")
DayLabel.configure(font = ("Helvetica", 12))
DayLabel.grid(column = 0, row = 6, padx = (0, 50), pady = (0, 0))

day = customtkinter.CTkOptionMenu(frame, values = valueDays, fg_color = "white", button_color = "#FF3131")
day.grid(column = 4, row = 6, pady = (25, 25))

MonthLabel = customtkinter.CTkLabel(frame, text = "Month")
MonthLabel.configure(font = ("Helvetica", 12))
MonthLabel.grid(column = 0, row = 7, padx = (0, 50), pady = (0, 25))

month = customtkinter.CTkOptionMenu(frame, values = valueMonth, fg_color = "white", button_color = "#FF3131")
month.grid(column = 4, row = 7, pady = (0, 25))

yearLabel = customtkinter.CTkLabel(frame, text = "Year Of Birth")
yearLabel.configure(font = ("Helvetica", 12))
yearLabel.grid(column = 0, row = 8, padx = (0, 50), pady = (0, 25))

year = customtkinter.CTkOptionMenu(frame, values = valueYears, fg_color = "white", button_color = "#FF3131")
year.grid(column = 4, row = 8, pady = (0, 25))

BaseLabel = customtkinter.CTkLabel(frame, text = "Complete The Form", bg_color="#0096FF")
BaseLabel.grid(row = 9, column = 3)

CreateButton = customtkinter.CTkButton(frame, text = "Create Record", fg_color = "#FF3131", command = newPatient)
CreateButton.grid(column = 2, row = 10, pady = (25, 25))

BackButton = customtkinter.CTkButton(frame, text = "Search Records", fg_color = "#FF3131")
BackButton.grid(column = 4, row = 10, pady = (25, 25))

frame.pack(padx = 30, pady = 30)
root.mainloop()