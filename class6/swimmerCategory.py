from datetime import datetime


userBornYear = int(input("In what year were you born? \n"));
currentYear = datetime.today().year;
age = currentYear - userBornYear;

if(age <= 9):
    print("You're in the 'Little' category");
elif(age <= 14):
    print("You're in the 'Childish' category");
elif(age <= 19):
    print("You're in the 'Junior' category");
elif(age == 20):
    print("You're in the 'Senior' category");
else:
    print("You're in the 'Master' category");