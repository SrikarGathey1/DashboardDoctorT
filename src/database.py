import sqlite3




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
cur.execute("DROP TABLE patients")
connec.close()
        