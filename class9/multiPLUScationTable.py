while True:
    num = int(input("Enter the number that you want: \n"))
    if(num < 0):
        break
    for i in range(10):
        print(f"{num} x {i} = {num * i}")
