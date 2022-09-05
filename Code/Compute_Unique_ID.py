# To compute Unique ID for a person based on the details he enters.

def unique_id_compute(state, district, count):
    order = count + 1
    checksum = state + district + order
    stateStr = str(state).zfill(3)
    districtStr = str(district).zfill(2)
    orderStr = str(order).zfill(4)
    checksumStr = str(checksum).zfill(2)
    uniqueID = stateStr + districtStr + orderStr + checksumStr
    return uniqueID

# print(unique_id_compute(7, 3, 8))
