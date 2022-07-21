# from math import floor, sqrt

# num = int(input("Enter the number that you want: \n"))
# currentNum = 0

# while currentNum != num:
#     calculateNumberInFibonacciSequence = ((1.618034) ** currentNum - (1-1.618034) ** currentNum) / sqrt(5)
#     print(floor(calculateNumberInFibonacciSequence), end=' → ')
#     currentNum += 1
# print("OVER")

print("=-" * 30)
print("Fibonacci Sequence")
print("=-" * 30)

num = int(input("Enter the amount of terms that you want: \n"))
t1 = 0
t2 = 1

currentNumber = 0
while(currentNumber != num):
    print(t1 + t2, end=' → ')
    sT = t1 + t2
    t1 = t2
    t2 = sT
    currentNumber += 1
print("OVER")