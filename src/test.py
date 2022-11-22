import sqlite3

conn = sqlite3.connect("records.db")

c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS account(email TEXT PRIMARY KEY, password TEXT)""")

# c.execute("INSERT INTO account VALUES(?, ?)", ('venkatnaras123@gmail.com', 'BossFan123'))



# c.execute("""CREATE TABLE IF NOT EXISTS patient_list(uniqueid TEXT PRIMARY KEY, email TEXT, fname TEXT, mname TEXT, lname TEXT, phone INTEGER, weight INTEGER, height INTEGER, gender TEXT, day INTEGER, month INTEGER, year INTEGER)""")
# Order:
# 1. uniqueid text
# 2. email text
# 3. fname text
# 4. mname text
# 5. lname text 
# 6. phone int
# 7. weight int
# 8. height int
# 9. gender int
# 10. day int
# 11. month int
# 12. year int


# c.execute("INSERT INTO patient_list VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", ("P984770498710", "venkatnaras123@gmail.com", "Srikar", "", "Gade", 9597216381, 76, 182, "Male", 17, 4, 2000))

# c.execute("SELECT * FROM patient_list")
# for item in c.fetchall():
  # print(item)

# c.execute("DELETE FROM patient_list WHERE email != ?", ("venkatnaras123@gmail.com", ))

c.execute("SELECT * FROM patient_list")
for item in c.fetchall():
  print(item)

# c.execute("SELECT * FROM account")
# for item in c.fetchall():
#  print(item)

conn.commit()
 


