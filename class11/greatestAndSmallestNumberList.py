values = []
greatestNumber = ""
smallestNumber = ""

for x in range(5):
    userNum = int(input("Enter a value: "))
    if(greatestNumber == "" or greatestNumber < userNum):
        greatestNumber = userNum
    if(smallestNumber == "" or smallestNumber > userNum):
        smallestNumber = userNum
    values.append(userNum)

print(f"The greatest value you entered was {greatestNumber} in position(s): ", end='')
for pos, num in enumerate(values):
    if(num == greatestNumber):
        print(pos, end='... ')

print(f"\nThe smallest value you entered was {smallestNumber} in position(s): ", end='')
for pos, num in enumerate(values):
    if(num == smallestNumber):
        print(pos, end='... ')