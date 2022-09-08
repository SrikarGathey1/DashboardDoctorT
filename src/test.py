import sqlite3

conn = sqlite3.connect("records.db")

c = conn.cursor()

c.execute("SELECT stateID FROM states where name = ?", ("Andhra Pradesh",))
print(c.fetchall()[0][0])
conn.close()
