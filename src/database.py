import sqlite3

# Connect to a database
conn = sqlite3.connect("records.db")

# Create a cursor 
curs = conn.cursor()

# Creating a table
# curs.execute(""" CREATE TABLE patients (
#            uniqueID text,
#            name text,
#            email text,
#            state number,
#            dob number )
#            """)



# Creating States and Numbers table.
# curs.execute("CREATE TABLE states(stateID number PRIMARY KEY, name text)")

# Inserting values in States Table.
# while 1:
#    stateID = int(input("Enter State id:"))
#    name = input("Enter state name:")
#    curs.execute("INSERT INTO states VALUES(?, ?)", (stateID, name))
#    flag = int(input("Do you wish to continue?"))
#    if flag == 1:
#        break
#    else:
#        continue

# curs.execute("SELECT * FROM states")
# print(curs.fetchall())

# Adding a record
# curs.execute("INSERT INTO patients VALUES('00117000927', 'Srikar Gade', 'venkatnaras123@gmail.com', 1, 17)")
# curs.execute("INSERT INTO patients VALUES('00817004671', 'John Brown', 'john.brown@gmail.com', 8, 17)")
# curs.execute("INSERT INTO patients VALUES('02409003871', 'Matt Smith', 'matt.smith1@gmail.com', 24, 9)")
 

# Displaying the table patients
# curs.execute("SELECT rowid, * FROM patients")
# print(curs.fetchall())
# print("Unique ID\t\t", "Name\t\t", "Email\t\t", "State\t\t", "Date Of Birth")
# for item in curs.fetchall():
#    print(item[0], "\t\t", item[1], "\t", item[2], item[3], item[4])

# Fetching Name of Patient and the State they are from.
#curs.execute("SELECT p.name, s.name FROM patients p, states s where s.stateID = p.state")
# print(curs.fetchall())

# Commiting our command
conn.commit()

# Close our connection
conn.close()