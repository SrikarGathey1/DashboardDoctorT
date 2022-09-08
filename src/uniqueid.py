# To compute Unique ID for a person based on the details he enters.
import sqlite3

def unique_id_compute(name, year, count):
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT stateID FROM states WHERE name = ?", (name,))
    state = cursor.fetchall()[0][0]
    order = count + 1
    checksum = state + (year % 100) + order
    stateStr = str(state).zfill(3)
    yearStr = str(year % 100).zfill(2)
    orderStr = str(order).zfill(4)
    checksumStr = str(checksum).zfill(2)
    uniqueID = stateStr + yearStr + orderStr + checksumStr
    conn.close()
    return uniqueID

# print(unique_id_compute("Andhra Pradesh", 1988, 4))
# 01920004584
# 01720000239
# 034880005127


# State - Number corresponding to the state the person is from.
# Year - Number corresponding to the day of the person's birth.
# Count - The number of people in the database from the same state and district.
# Checksum - Sum of all three values for checking and validating the ID.

