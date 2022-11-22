from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk

root = Tk()

canvas = Canvas(root, width=300, height=300, bg='white')
x0 = 20
x1 = 200
y0 = 20
y1 = 200
w2 = 5


custom_font = tkFont.Font(family="Helvetica", size=12, weight='bold')


canvas.create_oval(x0 + w2, y0 + w2, x1 - w2, y1 - w2, outline = "grey")

canvas.create_oval(x0 - w2, y0 - w2, x1 + w2, y1 + w2, outline = "grey")


canvas.grid(row = 1, column = 0 , rowspan = 2, columnspan = 2, padx = 10, pady = 10)

root.mainloop()