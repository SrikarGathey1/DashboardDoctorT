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
        self.unique = "P984770498710" 
        self.breathAnalyze(self.unique)
        # Create a main frame


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



root = customtkinter.CTk()
App(root)
root.eval("tk::PlaceWindow . center")
root.mainloop()