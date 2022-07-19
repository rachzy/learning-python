num = int(input("Enter a number: \n"))

isPrime = True
for x in range(1, num + 1):
    if(num % x == 0):
        print(f"\033[92m{x}", end=' ')
        if(x != 1 and x != num):
            isPrime = False
    else:
        print(f"\033[91m{x}", end=' ')

if(isPrime):
    print("\n\033[mThis number is prime")
else:
    print("\n\033[mThis number isn't prime")
