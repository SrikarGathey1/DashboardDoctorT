import sqlite3
from re import *


def searchRecords(searchStr):
    searchResults = []
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patient_list")
    items = cursor.fetchall()
    for item in items:
        name = item[1]
        phone = str(item[2])
        if searchStr in item[1]:
            if item in searchResults:
                continue
            else:
                searchResults.append(item)
        if searchStr in phone:
            if item in searchResults:
                continue
            else:
                searchResults.append(item)
        if searchStr in item[0]:
            if item in searchResults:
                continue
            searchResults.append(item)
    return searchResults

searchStr = "77"
print(searchRecords(searchStr))