import sqlite3
from tkinter import *
from uniqueid import *
from random import *
import re

def loginUser():
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM account")
    user = username.get()
    pwd = password.get()
    print(user, pwd)
    accounts = cursor.fetchall()

