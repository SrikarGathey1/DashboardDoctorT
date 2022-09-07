# To compute Unique ID for a person based on the details he enters.

def unique_id_compute(state, year, count):
    order = count + 1
    checksum = state + year + order
    stateStr = str(state).zfill(3)
    yearStr = str(year).zfill(2)
    orderStr = str(order).zfill(4)
    checksumStr = str(checksum).zfill(2)
    uniqueID = stateStr + yearStr + orderStr + checksumStr
    return uniqueID

print(unique_id_compute(19, 20, 44))
# 01920004584


# State - Number corresponding to the state the person is from.
# Year - Number corresponding to the day of the person's birth.
# Count - The number of people in the database from the same state and district.
# Checksum - Sum of all three values for checking and validating the ID.

