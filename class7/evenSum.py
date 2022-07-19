sum = 0
counter = 0
for i in range(0, 6):
    num = int(input("Enter a number: \n"))
    if(num % 2 == 0):
        sum += num
        counter += 1
print(f"The sum of the {counter} numbers is equal to {sum}")
