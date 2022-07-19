num = int(input("Enter the number: "))
interval = int(input("Enter the interval: "))
tenth = num + (10 - 1) * interval

for i in range(num, tenth, interval):
    print(i, end=' → ')
print("OVER!")
