numbers = [[], []]
for x in range(7):
    num = int(input("Enter a number: "))
    if(num % 2 == 0):
        numbers[0].append(num)
    else:
        numbers[1].append(num)

print(f"The even numbers you entered were: {sorted(numbers[0])}")
print(f"The odd numbers you entered were: {sorted(numbers[1])}")