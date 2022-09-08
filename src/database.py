import sqlite3
from uniqueid import *

class Patient:
    def __init__(self):
        self.conn = sqlite3.connect("records.db")
        self.cur = self.conn.cursor()

    def insertRecord(self):
        self.firstName = input("Enter the first name of the patient:")
        self.lastName = input("Enter the last name of the patient:")
        self.emailID = input("Enter the email id of the patient:")
        self.stateName = input("Enter the State the patient is from:")
        self.day = int(input("Enter the day of birth of the patient:"))
        self.month = int(input("Enter the month of birth of the patient:"))
        self.year = int(input("Enter the year of birth of the patient:"))
        self.uniqueID = unique_id_compute(self.stateName, self.year, 6)
        self.cur.execute(""" INSERT INTO patients VALUES(?, ?, ?, ?, ?, ?, ?, ?)
                        """, (self.uniqueID, self.firstName, self.lastName, self.emailID, self.stateName, self.day, self.month, self.year))
    
    def displayTable(self):
        self.cur.execute("SELECT * FROM PATIENTS")
        items =self.cur.fetchall()
        for item in items:
            print(item)
        self.conn.commit()
        self.conn.close()
        


class State:
    def __init__(self):
        conn = sqlite3.connect("records.db")
        self.cur = conn.cursor()

    def stateNumber(self, name):
        self.cur.execute("SELECT stateID FROM states WHERE name = ?", (name,))
        print(self.cur.fetchall())
    
    def stateName(self, stateID):
        self.cur.execute("SELECT name FROM states WHERE stateID = ?", (stateID,))
        print(self.cur.fetchall())

    def displayStates(self):
        self.cur.execute("SELECT * FROM states")
        print(self.cur.fetchall())



# cursor.execute("""  CREATE TABLE patients(
#                    uniqueID TEXT PRIMARY KEY,
#                    firstName TEXT,
#                    lastName TEXT,
#                    emailID TEXT,
#                    stateName TEXT,
#                    day INTEGER,
#                    month INTEGER,
#                    year INTEGER)""")
# cursor.execute("SELECT * FROM patients")
p = Patient()
# p.insertRecord()
p.displayTable()
