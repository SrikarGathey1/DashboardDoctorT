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
cur.execute("UPDATE patients SET day = 17 WHERE state = 1")
p.displayTable()
        