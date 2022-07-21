num = int(input("Enter the number: "))
interval = int(input("Enter the interval: "))
tenth = num + (10 - 1) * interval

while num != tenth:
    print(num, end=' → ')
    num += interval
print("OVER!")
