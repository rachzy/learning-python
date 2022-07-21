num = int(input("Enter a number: \n"))

print("Factoring this number is equal to: ")
finalMultiplication = 1

while num > 0:
    print(num, end='')
    print(' x ' if num > 1 else ' = ', end='')
    finalMultiplication *= num
    num -= 1
print(finalMultiplication)
