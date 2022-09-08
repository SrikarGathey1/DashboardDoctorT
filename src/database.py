import sqlite3

class Patient:
    def __init__(self):
        conn = sqlite3.connect("records.db")
        self.cur = conn.cursor()

    def insertRecord(self, uniqueID, firstName, lastName, emailID, stateName, day, month, year):
        self.cur.execute(""" INSERT INTO patients VALUES(?, ?, ?, ?, ?, ?, ?, ?)
                        """, (uniqueID, firstName, lastName, emailID, stateName, day, month, year))
    
    def displayTable(self):
        self.cur.execute("SELECT * FROM PATIENTS")
        print(self.cur.fetchall())

        


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
# p.insertRecord('01720000239', 'Srikar', 'Gade', 'venkatnaras123@gmail.com', 'Andhra Pradesh', 17, 4, 2000)
p.displayTable()