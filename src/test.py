import sqlite3

conn = sqlite3.connect("records.db")

c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS account(email TEXT PRIMARY KEY, password TEXT)""")

# c.execute("INSERT INTO account VALUES(?, ?)", ('venkatnaras123@gmail.com', 'BossFan123'))

# c.execute("SELECT * FROM account")

# print(c.fetchall())

c.execute("""CREATE TABLE IF NOT EXISTS patient_list(uniqueid TEXT PRIMARY KEY, name TEXT, phone INTEGER, weight INTEGER, height INTEGER, gender TEXT, day INTEGER, month INTEGER, year INTEGER)""")
# Order:
# 1. uniqueid text
# 2. name text
# 3. phone int
# 4. weight int 
# 5. height int
# 6. gender text
# 7. day int
# 8. month int
# 9. year int

# c.execute("INSERT INTO patient_list VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", ("01720000239", "Srikar Gade", 9597216381, 76, 182, "Male", 17, 4, 2000))

c.execute("SELECT * FROM patient_list")
for item in c.fetchall():
    print(item)
    break

conn.commit()

conn.close()
 


