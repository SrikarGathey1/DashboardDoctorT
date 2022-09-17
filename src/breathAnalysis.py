import sqlite3
from tkinter import *
from turtle import bgcolor, color
from PIL import *
import customtkinter

root = Tk()
root.configure(bg = "white")


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

######### TITLE FRAME #################

TitleFrame = customtkinter.CTkFrame(root, width = 50, height = 50, bg_color = "white", fg_color = "white")

TitleLabel = customtkinter.CTkLabel(TitleFrame, text = "BREATH ANALYSIS", text_color = "black")
TitleLabel.configure(font = ("Oswald", 15))
TitleLabel.grid(column = 0, row = 0, rowspan = 3, pady = (10, 10), ipadx = 5, ipady = 5)


TitleFrame.pack(padx = 100, pady = 10)


######## INFO FRAME ##################

InfoFrame = customtkinter.CTkFrame(root, width = 450, height = 750, bg_color = "white", fg_color = "white")

conn = sqlite3.connect("records.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM patient_list")
for item in cursor.fetchall():
    break


patientNo = customtkinter.CTkLabel(InfoFrame, text = "Patient No: " + item[0])
patientNo.configure(font = ("Oswald", 10))
patientNo.grid(row = 0, column = 1, pady = 10, padx = 10)

patientName = customtkinter.CTkLabel(InfoFrame, text = item[1])
patientName.configure(font = ("Oswald", 20))
patientName.grid(row = 1, column = 0, columnspan = 2,  pady = 10)

Age = customtkinter.CTkLabel(InfoFrame, text = str(2022 - item[-1]) + " years")
Age.configure(font = ("Oswald", 10))
Age.grid(row = 1, column = 2, pady = 10, padx = 10)

Gender = customtkinter.CTkLabel(InfoFrame, text = item[5])
Gender.configure(font = ("Oswald", 10))
Gender.grid(row = 2, column = 0, pady = 10, padx = 10)

Height = customtkinter.CTkLabel(InfoFrame, text = str(item[4]) + "cms")
Height.configure(font = ("Oswald", 10))
Height.grid(row = 2, column = 1, pady = 10, padx = 10)

Weight = customtkinter.CTkLabel(InfoFrame, text = str(item[3]) + "Kgs")
Weight.configure(font = ("Oswald", 10))
Weight.grid(row = 2, column = 2, pady = 10, padx = 10)


InfoFrame.pack(pady = (50, 100), padx = (10, 10))

############ Buttons Frame ####################

ButtonFrame = customtkinter.CTkFrame(root, width = 150, height = 400, fg_color = "white")

DeviceLabel = customtkinter.CTkLabel(ButtonFrame, text = "Select DrT Device:")
DeviceLabel.configure(font = ("Oswald", 10))
DeviceLabel.grid(row = 0, column = 0, pady = 20, padx = 20)


DropDown = customtkinter.CTkOptionMenu(ButtonFrame, values = ["DR-T-ALPHA01", "DR-T-BETA01"], fg_color = "white", button_color = "#0096FF")
DropDown.grid(row = 0, column = 1, pady = 20, padx = 40)

SetDeviceLabel = customtkinter.CTkButton(ButtonFrame, text = "Set Device", fg_color = "#0096FF", text_font = ("Oswald", 10))
SetDeviceLabel.grid(row = 0, column = 2, pady = 20, padx = 40)

DurationLabel = customtkinter.CTkLabel(ButtonFrame, text = "Duration(Secs):")
DurationLabel.configure(font = ("Oswald", 10))
DurationLabel.grid(row = 1, column = 0, pady = 20, padx = 40)

TimeDropDown = customtkinter.CTkOptionMenu(ButtonFrame, values = ["10", "20", "30"], fg_color = "white", button_color = "#0096FF")
TimeDropDown.grid(row = 1, column = 1, pady = 20, padx = 40)

ResetDeviceButton = customtkinter.CTkButton(ButtonFrame, text = "Reset Device", fg_color = "#0096FF", text_font = ("Oswald", 10))
ResetDeviceButton.grid(row = 1, column = 2, pady = 20, padx = 40)

NormalImage = PhotoImage(file = "normal.png")
NormalLabel = customtkinter.CTkButton(ButtonFrame, text = "Normal", fg_color = "#0096FF", image = NormalImage, text_font = ("Oswald", 10))
NormalLabel.grid(row = 2, column = 0, pady = 20, padx = 40)

MediumImage = PhotoImage(file = "medium.png")
MediumLabel = customtkinter.CTkButton(ButtonFrame, text = "Medium", fg_color = "#0096FF", image = MediumImage, text_font = ("Oswald", 10))
MediumLabel.grid(row = 2, column = 1, pady = 20, padx = 40)

HeavyImage = PhotoImage(file = "heavy.png")
HeavyLabel = customtkinter.CTkButton(ButtonFrame, text = "Heavy", fg_color = "#0096FF", image = HeavyImage, text_font = ("Oswald", 10))
HeavyLabel.grid(row = 2, column = 2, pady = 20, padx = 40)


ButtonFrame.pack(pady = (0, 50), padx = (10, 10))

############################### TIMER FRAME ##################################################

############################### Save and Analyze and Back Buttons Frame ######################################
FrameBack = customtkinter.CTkFrame(root, width = 200, height = 200, fg_color = "white")

AnalyzeImage = PhotoImage(file = "analyze_save.png")
AnalyzeButton = customtkinter.CTkButton(FrameBack, text = "Analyze And Save", fg_color = "#0096FF", image = AnalyzeImage, text_font = ("Oswald", 10))
AnalyzeButton.grid(row = 0, column = 0, padx = 10, ipadx = 5, ipady = 5)

BackImage = PhotoImage(file = "back_arrow.png")
BackButton = customtkinter.CTkButton(FrameBack, text = "Back To Search", fg_color = "#0096FF", image = BackImage, text_font = ("Oswald", 10))
BackButton.grid(row = 0, column = 1, padx = 10, ipadx = 5, ipady = 5)

FrameBack.pack(padx = 200)



root.eval("tk::PlaceWindow . center")
root.mainloop()