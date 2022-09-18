from email.mime import image
from tkinter import ttk
import sqlite3
import ctypes
from tkinter import *
from turtle import bgcolor, color
from PIL import Image
from PIL import ImageTk
from PIL import *
import customtkinter
import matplotlib.pyplot as plt
import numpy
from scipy import *



 # >= win 8.1
ctypes.windll.shcore.SetProcessDpiAwareness(2)


# plt.plot(time, amplitude)


root = Tk()
root.configure(bg = "black")

conn = sqlite3.connect("records.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM patient_list")
for item in cursor.fetchall():
    break

########################## First Frame ###############################


frame1 = customtkinter.CTkFrame(root, width = 150, height = 200, fg_color = "black")

TitleLabel = customtkinter.CTkLabel(frame1, text = "ANALYSIS REPORT", text_color = "white")
TitleLabel.configure(font = ("Oswald", 15))
TitleLabel.grid(column = 0, row = 0, columnspan = 3, padx = 10, pady = 10)

NameLabel = customtkinter.CTkLabel(frame1, text = item[1], text_color = "white")
NameLabel.configure(font = ("Oswald", 10))
NameLabel.grid(column = 0, row = 1, padx = 10, pady = 10)

AgeLabel = customtkinter.CTkLabel(frame1, text = str(2022 - item[-1]) + " years", text_color = "white")
AgeLabel.configure(font = ("Oswald", 10))
AgeLabel.grid(column = 1, row = 1, padx = 10, pady = 10)

IDLabel = customtkinter.CTkLabel(frame1, text = "PID: " + item[0], text_color = "white")
IDLabel.configure(font = ("Oswald", 10))
IDLabel.grid(column = 2, row = 1, padx = 10, pady = 10)

WeightLabel = customtkinter.CTkLabel(frame1, text = str(item[3]) + " Kg", text_color = "white")
WeightLabel.configure(font = ("Oswald", 10))
WeightLabel.grid(column = 0, row = 2, padx = 10, pady = 10)

HeightLabel = customtkinter.CTkLabel(frame1, text = str(item[4]) + "cm", text_color = "white")
HeightLabel.configure(font = ("Oswald", 10))
HeightLabel.grid(column = 1, row = 2, padx = 10, pady = 10)

GenderLabel = customtkinter.CTkLabel(frame1, text = item[5], text_color = "white")
GenderLabel.configure(font = ("Oswald", 10))
GenderLabel.grid(column = 2, row = 2, padx = 10, pady = 10)


frame1.pack(padx = 10, pady = 10)

################ FRAME 2 ####################################

# img = Image.open('plot1.png')
# wpercent = (basewidth / float(img.size[0]))
# hsize = int((float(img.size[1]) * float(wpercent)))
# img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
# img.save('resized_plot1.png')

frame2 = customtkinter.CTkFrame(root, width = 600, height = 600, fg_color = "white")

filename = ImageTk.PhotoImage(file = "resized_plot1.png")
background_label = Label(frame2, image=filename)

background_label.grid(row = 0, column = 0)

frame2.pack(pady = 25, padx = 10)

############ FRAME 3 ########################################

wid = 300
hei = 100
frame3 = customtkinter.CTkFrame(root, width = 3 * wid, height = 2 * hei, fg_color = "black")

RespiratoryFrame = customtkinter.CTkFrame(frame3, width = wid, height = hei, fg_color = "black")

TitleLabel = customtkinter.CTkLabel(RespiratoryFrame, text = "50 cycles/min", text_color = "white")
TitleLabel.configure(font = ("Oswald", 14))
TitleLabel.grid(column = 0, row = 0, padx = 10, pady = 10)

CaptionLabel = customtkinter.CTkLabel(RespiratoryFrame, text = "Respiration Rate", text_color = "grey")
CaptionLabel.configure(font = ("Oswald", 8))
CaptionLabel.grid(column = 0, row = 1, padx = 10)

RespiratoryFrame.grid(column = 0, row = 0, padx = 40)

RespiratoryFrame = customtkinter.CTkFrame(frame3, width = wid, height = hei, fg_color = "black")

TitleLabel = customtkinter.CTkLabel(RespiratoryFrame, text = "50 m/sec", text_color = "white")
TitleLabel.configure(font = ("Oswald", 14))
TitleLabel.grid(column = 0, row = 0, padx = 10, pady = 10)

CaptionLabel = customtkinter.CTkLabel(RespiratoryFrame, text = "Mean Inspiration Velocity", text_color = "grey")
CaptionLabel.configure(font = ("Oswald", 8))
CaptionLabel.grid(column = 0, row = 1, padx = 10)

RespiratoryFrame.grid(column = 1, row = 0, padx = 40)

RespiratoryFrame = customtkinter.CTkFrame(frame3, width = wid, height = hei, fg_color = "black")

TitleLabel = customtkinter.CTkLabel(RespiratoryFrame, text = "50 m/sec", text_color = "white")
TitleLabel.configure(font = ("Oswald", 14))
TitleLabel.grid(column = 0, row = 0, padx = 10, pady = 10)

CaptionLabel = customtkinter.CTkLabel(RespiratoryFrame, text = "Mean Expiration Velocity", text_color = "grey")
CaptionLabel.configure(font = ("Oswald", 8))
CaptionLabel.grid(column = 0, row = 1, padx = 10)

RespiratoryFrame.grid(column = 2, row = 0, padx = 40)

RespiratoryFrame = customtkinter.CTkFrame(frame3, width = wid, height = hei, fg_color = "black")

TitleLabel = customtkinter.CTkLabel(RespiratoryFrame, text = "50 Liters/sec", text_color = "white")
TitleLabel.configure(font = ("Oswald", 14))
TitleLabel.grid(column = 0, row = 0, padx = 10, pady = 10)

CaptionLabel = customtkinter.CTkLabel(RespiratoryFrame, text = "Mean Inspiration Volume", text_color = "grey")
CaptionLabel.configure(font = ("Oswald", 8))
CaptionLabel.grid(column = 0, row = 1, padx = 10)

RespiratoryFrame.grid(column = 0, row = 1, padx = 40)

RespiratoryFrame = customtkinter.CTkFrame(frame3, width = wid, height = hei, fg_color = "black")

TitleLabel = customtkinter.CTkLabel(RespiratoryFrame, text = "50 Liters/sec", text_color = "white")
TitleLabel.configure(font = ("Oswald", 14))
TitleLabel.grid(column = 0, row = 0, padx = 10, pady = 10)

CaptionLabel = customtkinter.CTkLabel(RespiratoryFrame, text = "Mean Expiration Volume", text_color = "grey")
CaptionLabel.configure(font = ("Oswald", 8))
CaptionLabel.grid(column = 0, row = 1, padx = 10)

RespiratoryFrame.grid(column = 1, row = 1, padx = 40)

RespiratoryFrame = customtkinter.CTkFrame(frame3, width = wid, height = hei, fg_color = "black")

TitleLabel = customtkinter.CTkLabel(RespiratoryFrame, text = "50 Liters/sec", text_color = "white")
TitleLabel.configure(font = ("Oswald", 14))
TitleLabel.grid(column = 0, row = 0, padx = 10, pady = 10)

CaptionLabel = customtkinter.CTkLabel(RespiratoryFrame, text = "Mean Tidal Volume", text_color = "grey")
CaptionLabel.configure(font = ("Oswald", 8))
CaptionLabel.grid(column = 0, row = 1, padx = 10)

RespiratoryFrame.grid(column = 2, row = 1, padx = 40)


frame3.pack(pady = 25, padx = 10)

FrameBack = customtkinter.CTkFrame(root, width = 150, height = 150, fg_color = "#0096FF") 

BackButton = customtkinter.CTkButton(FrameBack, text = "Back To Search", fg_color = "#0096FF", text_font = ("Oswald", 10))
BackButton.grid(row = 0, column = 0, padx = 10, ipadx = 5, ipady = 5)

FrameBack.pack()

root.eval("tk::PlaceWindow . center")
root.mainloop()

