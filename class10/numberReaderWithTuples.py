n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))
n4 = int(input("Enter a number: "))

numbers = (n1, n2, n3, n4)
amountOfEven = 0

for x in numbers:
    if(x % 2 == 0):
        amountOfEven += 1

print(f"You entered the values: {numbers}")
print(f"The number 9 appeared {numbers.count(9)} times")
print(f"The first number 3 appeared in the position: {numbers.index(3)}")
print(f"The amount of even numbers entered was: {amountOfEven}")