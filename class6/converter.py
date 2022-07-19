num = int(input("Type the number that you wanna convert: \n"))
conversionType = int(input(
    "What kind of conversion you wanna make? \n 1- Binary \n 2- Octal \n 3- Hexadecimal \n"))

if(conversionType == 1):
    print("You choosed BINARY")
    print(f"This number in binary is equal to: {bin(num)}")
elif(conversionType == 2):
    print("You choosed OCTAL")
    print(f"This number in octal is equal to: {oct(num)}")
elif(conversionType == 3):
    print("You choosed HEXADECIMAL")
    print(f"This number in Hexadecimal is equal to: {hex(num)}")
else:
    print("You choosed an invalid option.")