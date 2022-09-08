import sqlite3

conn = sqlite3.connect("records.db")

c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS account(email TEXT PRIMARY KEY, password TEXT)""")

# c.execute("INSERT INTO account VALUES(?, ?)", ('venkatnaras123@gmail.com', 'BossFan123'))

c.execute("SELECT * FROM account")

print(c.fetchall())

conn.commit()

conn.close()
