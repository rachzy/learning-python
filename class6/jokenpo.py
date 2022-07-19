from random import randint

print("-=" * 20);
print("JOKENPO");
print("-=" * 20);

print("Let's play! You VS Me (PC) >:) \n");
userChoice = int(input("Choose: \n [ 1 ] Stone \n [ 2 ] Paper \n [ 3 ] Scissor \n"));

print("JO");
print("KEN");
print("PO!!! \n");

computerChoice = randint(1, 3);

choices = ["Stone", "Paper", "Scissor"];

if(userChoice == computerChoice):
    print("-=" * 20);
    print("IT'S A TIE!");
    print("-=" * 20);
elif((userChoice == 1 and computerChoice != 2) 
    or (userChoice == 2 and computerChoice != 3) 
    or (userChoice == 3 and computerChoice != 1)):

    print("-=" * 20);
    print("YOU WON!");
    print("-=" * 20);

    print("Crap! You won! Congratulations >:/");
else:
    print("-=" * 20);
    print("YOU LOST!");
    print("-=" * 20);
    print("Haha! I won! >:)");
print(f"INFO: You choosed {choices[userChoice - 1]} and I choosed {choices[computerChoice - 1]}")