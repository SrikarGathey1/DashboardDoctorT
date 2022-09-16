# To compute Unique ID for a person based on the details he enters.
import sqlite3
from random import *


def unique_id_compute(name, year):
    if len(name) == 0:
        name = "a"
    state = ord(name[0])
    order = randint(1, 1000)
    checksum = state + (year % 100) + order
    stateStr = str(state).zfill(3)
    yearStr = str(year % 100).zfill(2)
    orderStr = str(order).zfill(4)
    checksumStr = str(checksum).zfill(2)
    uniqueID = stateStr + yearStr + orderStr + checksumStr
    return uniqueID


# 01920004584
# 01720000239
# 034880005127


# State - Number corresponding to the state the person is from.
# Year - Number corresponding to the day of the person's birth.
# Count - The number of people in the database from the same state and district.
# Checksum - Sum of all three values for checking and validating the ID.

