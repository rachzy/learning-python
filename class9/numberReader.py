amountOfEnteredNumbers = 0
sumOfEnteredNumbers = 0
while True:
    num = int(input("Enter a number: \n"))
    if(num == 999):
        break
    amountOfEnteredNumbers += 1
    sumOfEnteredNumbers += num
    
print(f"You entered {amountOfEnteredNumbers} numbers")
print(
    f"The sum of all the numbers you entered is equal to: {sumOfEnteredNumbers}")
