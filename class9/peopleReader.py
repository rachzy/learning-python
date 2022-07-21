amountOfPeopleThatAreMoreThan18 = amountOfRegisteredMen = amountOfWomenUnder20 = 0
while True:
    age = int(input("Enter the person's age: "))

    gender = ""
    while gender != "M" and gender != "F" and gender != "NB":
        gender = str(input("Enter the person's gender (M/F/NB): ")).upper()


    if(age > 18):
        amountOfPeopleThatAreMoreThan18 += 1
    if(gender == "M"):
        amountOfRegisteredMen += 1
    if(gender == "F" and age < 20):
        amountOfWomenUnder20 += 1
    
    choice = ""
    while choice != "Y" and choice != "N":
        choice = str(input("Do you wanna keep entering data? (Y/N) ")).upper()

    if choice == "N":
        break
print(f"-Amount of people that are more than 18: {amountOfPeopleThatAreMoreThan18}")
print(f"-Amount of people that are men: {amountOfRegisteredMen}")
print(f"-Amount of women that are under 20: {amountOfWomenUnder20}")
    