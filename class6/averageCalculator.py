grade1 = float(input("What was your first grade? \n"))
grade2 = float(input("What was your second grade? \n"))
av = (grade1 + grade2) / 2

if(av < 5):
    print("Sorry bro, you're reproved :/")
elif(av < 7):
    print("Oops, you'll have summer school, sorry :/")
else:
    print("You got approved, noice")
