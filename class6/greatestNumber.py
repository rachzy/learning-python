firstNum = int(input("Type the first number (integer): \n"))
secondNum = int(input("Type the second number (integer): \n"))

if(firstNum > secondNum):
    print(f"The first number ({firstNum}) is greater than the second one ({secondNum})")
elif(secondNum > firstNum):
    print(f"The second number ({secondNum}) is greater than the first one ({firstNum})")
else:
    print("Both numbers are equal")
