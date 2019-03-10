idNumber = '881120- 10668234'

###'012345-7890123

idNumber = idNumber.replace('-', '')
idNumber = idNumber.replace(' ', '')

###print(idNumber)

print(idNumber[0:6] , idNumber[6:])


string = "a:b:c:d"

print("#".join(string.split(":")))
