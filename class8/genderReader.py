gender = gender = str(input("Enter your gender (M/F/NB): \n")).upper()
while (gender != "M" and gender != "F" and gender != "NB"):
    gender = str(input("Invalid option! Please, enter your gender (M/F/NB): \n")).upper()
print(f"Your gender is {gender}")
