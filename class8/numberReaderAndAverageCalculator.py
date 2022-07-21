num = int(input("Enter a number: \n"))
choice = str(input("Wanna keep entering values? (Y/N) \n"))

amountOfEnteredNumbers = 0
sumOfEnteredNumbers = 0

greatestNumber = num
smallestNumber = num

while(choice == "Y"):
    amountOfEnteredNumbers += 1
    sumOfEnteredNumbers += num
    num = int(input("Enter a number: \n"))
    if(num > greatestNumber):
        greatestNumber = num
    elif(num < smallestNumber):
        smallestNumber = num
    choice = str(input("Wanna keep entering values? (Y/N) \n")).upper()

average = sumOfEnteredNumbers / amountOfEnteredNumbers
print(f"-The average of all the numbers you entered is {average:.1f}")
print(f"-The greatest number you entered was {greatestNumber}")
print(f"-The average of all the numbers you entered is {smallestNumber}")