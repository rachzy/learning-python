ages = 0
oldestMan = ["", 0]
womenWithLessThan20YearsOld = 0

for i in range(4):
    print('-' * 6, end=' ')
    print(f"Person {i + 1}", end=' ')
    print('-' * 6)
    name = str(input("Name: ")).strip()
    age = int(input("Age: "))
    gender = str(input("Gender (M, F, NB, O): ")).strip().upper()

    ages += age
    if(gender == "M" and oldestMan[1] < age):
        oldestMan = [name, age]
    elif(gender == "F" and age < 20):
        womenWithLessThan20YearsOld += 1

print(f"-The age average of this group is: {ages / 4:.1f}")
print(
    f"-The oldest man in this group is: {oldestMan[0]}, with {oldestMan[1]} years old")
print(
    f"-There is/are {womenWithLessThan20YearsOld} women with less than 20 years old in this group")