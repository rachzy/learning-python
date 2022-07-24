from random import randint
from time import sleep


numbers = list()


def sumEven():
    sumOfEven = 0
    for num in numbers:
        if(num % 2 == 0):
            sumOfEven += num
    print(f"Sum all the even values of {numbers}, we have {sumOfEven}")


def sortRandom():
    print("Sorting 5 random values to append in the list:", end=' ')
    for i in range(5):
        randNum = randint(1, 10)
        numbers.append(randNum)
        print(randNum, end=' ')
        sleep(0.3)
    print("DONE!")
    sumEven()
sortRandom()