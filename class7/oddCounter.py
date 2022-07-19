sum = 0
count = 0
for i in range(1, 501, 2):
    if(i % 3 == 0):
        sum += i
        count += 1
print(f"The sum of all the {count} numbers is equal to {sum}")
 