import sqlite3
from tkinter import *
from turtle import bgcolor, color
from PIL import *
import customtkinter


root = customtkinter.CTk()
root.title("Doctor T: Know Your Breath")


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


filename = PhotoImage(file = "searchPage.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


################### DATABASE CODE BEGINS #############################

def searchRecords(searchStr): 
    for widget in ResultInterFrame.winfo_children():
        widget.destroy()
    searchResults = []
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patient_list")
    items = cursor.fetchall()
    for item in items:
        name = item[1]
        phone = str(item[2])
        if searchStr in item[1]:
            if item in searchResults:
                continue
            else:
                searchResults.append(item)
        if searchStr in phone:
            if item in searchResults:
                continue
            else:
                searchResults.append(item)
        if searchStr in item[0]:
            if item in searchResults:
                continue
            searchResults.append(item)
    index = 0
    for item in searchResults:
        UniqueLabel = customtkinter.CTkLabel(ResultInterFrame, text = item[0])
        UniqueLabel.configure(font = ("Oswald", 10))
        UniqueLabel.grid(row = index, column = 0, pady = 10, padx = 10)

        NameLabel = customtkinter.CTkLabel(ResultInterFrame, text = item[1])
        NameLabel.configure(font = ("Oswald", 10))
        NameLabel.grid(row = index, column = 1, pady = 10, padx = 10)

        ViewButton = customtkinter.CTkButton(ResultInterFrame, text = "View", text_font = ("Oswald", 10))
        ViewButton.grid(row = index, column = 2, pady = 10, padx = 10)
        index += 1
    if len(searchResults) == 0:
        NotFoundLabel = customtkinter.CTkLabel(ResultInterFrame, text = "No records found!!")
        NotFoundLabel.configure(font = ("Oswald", 15))
        NotFoundLabel.grid(row = 0, column = 0, columnspan = 3, padx = 200, pady = 50)

################### DATABASE ENDS ####################################

TitleFrame = customtkinter.CTkFrame(root, width = 500, height = 500, fg_color = "#6495ED")

InterFrame = customtkinter.CTkFrame(TitleFrame, width = 460, height = 460, fg_color = "#0047AB")

TitleLabel = customtkinter.CTkLabel(InterFrame, text = "SEARCH PATIENT RECORDS", text_color = "white")
TitleLabel.configure(font = ("Oswald", 15))
TitleLabel.grid(column = 0, row = 0, columnspan = 3, padx = 10, pady = 20)

SearchEntry = customtkinter.CTkEntry(InterFrame, placeholder_text = "Search for patients", width = 150)
SearchEntry.grid(column = 0, row = 1, padx = 10, pady = (0, 10))

SearchButton = customtkinter.CTkButton(InterFrame, text = "Search", text_font = ("Oswald", 10), command= lambda: searchRecords(SearchEntry.get()))
SearchButton.grid(column = 1, row = 1, padx = 10, pady = (0, 10))

CreateButton = customtkinter.CTkButton(InterFrame, text = "New Patient", text_font = ("Oswald", 10))
CreateButton.grid(column = 2, row = 1, padx = 10, pady = (0, 10))

InterFrame.pack(padx = 20, pady = 20) 

TitleFrame.pack(pady = 75)

ResultsFrame = customtkinter.CTkFrame(root, width = 500, height = 500, fg_color = "#6495ED")

ResultInterFrame = customtkinter.CTkFrame(ResultsFrame, width = 560, height = 560)

ResultInterFrame.pack(pady = 20, padx = 20)

ResultsFrame.pack(pady = 75)

root.eval('tk::PlaceWindow . center')
root.mainloop()