num = int(input("Enter a number: \n"))
amountOfEnteredNumbers = 0
sumOfEnteredNumbers = 0

while(num != 999):
    amountOfEnteredNumbers += 1
    sumOfEnteredNumbers += num
    num = int(input("Enter a number: \n"))
print(f"-You entered {amountOfEnteredNumbers} numbers \nThe sum of all this numbers is equal to: {sumOfEnteredNumbers}")
