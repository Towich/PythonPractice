def main(dictionary):
    b1 = int(dictionary['B1'])
    b2 = (int(dictionary['B2'])) << 3
    b3 = (int(dictionary['B3'])) << 11
    b4 = (int(dictionary['B4'])) << 20
    return int(b1 | b2 | b3 | b4)


#result = main({'B1': '2', 'B2': '56', 'B3': '42', 'B4': '0'})
#result = main({'B1': '6', 'B2': '252', 'B3': '355', 'B4': '1'})
result = main({'B1': '7', 'B2': '192', 'B3': '57', 'B4': '1'})
#result = main({'B1': '6', 'B2': '239', 'B3': '320', 'B4': '1'})
print(result)
