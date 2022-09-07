import sqlite3

conn = sqlite3.connect("records.db")

c = conn.cursor()

c.execute("SELECT * FROM patients")
print(c.fetchall())
