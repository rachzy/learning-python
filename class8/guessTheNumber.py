from random import randint

print("=-" * 10)
print("WELCOME TO GUESS THE NUMBER 2.0")
print("=-" * 10)

number = randint(1, 10)
print("I just thought of a number from 1 to 10... \n TRY TO GUESS IT!!")
tries = 0

# userNumber = int(input("I think the number is: \n"))
# while(userNumber != number):

isRight = False
while not isRight:
    print("Nope")
    tries += 1
    userNumber = int(input("I think the number is: \n"))
    if(userNumber == number):
        isRight = True
print(
    f"Well done! The number that I thought was {number}. \nYou did it in {tries} tries")
