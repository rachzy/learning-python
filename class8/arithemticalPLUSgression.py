num = int(input("Enter the number: "))
interval = int(input("Enter the interval: "))

currentNum = num
terms = 10

lastTerm = num + (terms - 1) * interval
userChoice = 1

while userChoice != 0:
    while currentNum != lastTerm:
        print(currentNum, end=' → ')
        currentNum += interval
    print("OVER!")
    userChoice = int(input("How many more terms do you want? "))
    terms += userChoice
    lastTerm = num + (terms - 1) * interval
print("Bye")  
