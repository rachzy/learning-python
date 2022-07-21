from random import randint


print("=-" * 20)
print("EVEN OR ODD")
print("=-" * 20)

amountOfVictories = 0

while True:
    num = int(input("\nEnter the number you want: "))
    choice = str(input("Even or Odd? (E/O): ")).upper()

    computerNum = randint(0, 100)

    numbersSum = num + computerNum
    if(choice != "E" and choice != "O"):
        print("You entered an invalid option")
        break
    if((choice == "E" and numbersSum % 2 != 0) or (choice == "O" and numbersSum % 2 == 0)):
        print("You lost! >:)")
        print(
            f"INFO: Number you entered: {num} // Number I thought of: {computerNum} // Sum of these numbers: {numbersSum}")
        break
    amountOfVictories += 1
    print("You won! Let's keep going!")
    print(
        f"INFO: Number you entered: {num} // Number I thought of: {computerNum} // Sum of these numbers: {numbersSum}")
print(f"You won {amountOfVictories} times!")
