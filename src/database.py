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

# Adding a record
# curs.execute("INSERT INTO patients VALUES('00117000927', 'Srikar Gade', 'venkatnaras123@gmail.com', 1, 17)")
# curs.execute("INSERT INTO patients VALUES('00817004671', 'John Brown', 'john.brown@gmail.com', 8, 17)")
# curs.execute("INSERT INTO patients VALUES('02409003871', 'Matt Smith', 'matt.smith1@gmail.com', 24, 9)")
 

# Displaying the table
curs.execute("SELECT * FROM patients")
# print("Unique ID\t\t", "Name\t\t", "Email\t\t", "State\t\t", "Date Of Birth")
# for item in curs.fetchall():
#    print(item[0], "\t\t", item[1], "\t", item[2], item[3], item[4])


# Commiting our command
conn.commit()

# Close our connection
conn.close()