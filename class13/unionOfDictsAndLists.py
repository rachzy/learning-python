people = list()
person = dict()

while True:
    print("=-" * 10)
    person["name"] = str(input("Name: "))
    person["age"] = int(input("Age: "))
    person["gender"] = str(input("Gender (M/F/NB): ")).upper()[0]
    people.append(person.copy())
    person.clear()

    choice = str(input("Wanna keep inserting data? [Y/N]: ")).upper()
    if(choice != "Y"):
        break

sumOfAges = 0
women = list()
for person in people:
    sumOfAges += person["age"]
    if(person["gender"] == "F"):
        women.append(person)

averageAge = sumOfAges / len(people)

print(f"You registered {len(people)} people")
print(f"The average of age of this group is {averageAge}")

print("=-" * 5, end=' ')
print("WOMEN", end=' ')
print("=-" * 5)

print("NAME", end=' ' * 6)
print("AGE")
for woman in women:
    print(woman["name"], end=' ' * (10 - len(woman["name"])))
    print(woman["age"])
print("=-" * 25)

print("\n")
print("=-" * 5, end=' ')
print("PEOPLE WITH AGE ABOVE AVERAGE", end=' ')
print("=-" * 5)

print("NAME", end=' ' * 6)
print("AGE")
for person in people:
    if(person["age"] > averageAge):
        print(person["name"], end=' ' * (10 - len(person['name'])))
        print(person["age"])