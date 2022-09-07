import sqlite3


class Patient:
    def __init__(self):
        conn = sqlite3.connect("records.db")
        self.c = conn.cursor()
        
    def insertRecord(self, uniqueID, name, email, state, dob):
        self.c.execute("INSERT INTO patients VALUES(?, ?, ?, ?, ?)", (uniqueID, name, email, state, dob))

    def displayTable(self):
        self.c.execute("SELECT * FROM patients")
        items = self.c.fetchall()
        for item in items:
            print(item)
    
    def deleteRecord(self, uniqueID):
        self.c.execute("DELETE FROM patients WHERE uniqueID = ?", (uniqueID,))


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

connec = sqlite3.connect("records.db")
cur = connec.cursor()
p = Patient()
# cursor.execute("ALTER TABLE patients ADD day number")
cur.execute("UPDATE patients SET day = 17, month = 4, dob = 2000 WHERE state = 1")
cur.execute("UPDATE patients SET day = 29, month = 9, dob = 1988 WHERE state = 8")
cur.execute("UPDATE patients SET day = 25, month = 12, dob = 1967 WHERE state = 24")
cur.execute("SELECT * FROM patients")
print(cur.fetchall())
        