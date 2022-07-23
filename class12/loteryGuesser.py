from random import randint
from time import sleep

guesses = []
amountOfGuesses = int(input("Enter the amount of guesses that you want me to do: "))

print("=-" * 5, end=' ')
print(f"SORTING {amountOfGuesses} GAMES", end=' ')
print("=-" * 5)
for i in range(amountOfGuesses):
    sleep(0.5)
    for j in range(6):
        randomNum = randint(1, 60)
        while randomNum in guesses:
            randomNum = randint(1, 60)
        guesses.append(randomNum)
    print(f"Game {i + 1}: {guesses}")
    guesses.clear()

print("=-" * 5, end=' ')
print("GOOD LUCK!", end= ' ')
print("=-" * 5)