people = []
person = []

highestWeight = []
lowestWeight = []

while True:
    person.append(str(input("Enter the persons name: ")))
    person.append(float(input("Enter the persons weight: ")))
    people.append(person[:])

    if(len(highestWeight) == 0):
        highestWeight.append(person[1])
        highestWeight.append(person[0])
        lowestWeight.append(person[1])
        lowestWeight.append(person[0])
    else:
        if(highestWeight[0] < person[1]):
            highestWeight[0] = person[1]
            highestWeight[1] = person[0]
        elif(highestWeight[0] == person[1]):
            highestWeight.append(person[0])

        if(lowestWeight[0] > person[1]):
            lowestWeight[0] = person[1]
            lowestWeight[1] = person[0]
        elif(lowestWeight[0] == person[1]):
            lowestWeight.append(person[0])

    person.clear()

    choice = str(input("Wanna keep inserting data? [Y/N] ")).upper()
    if(choice != "Y"):
        break

print(f"You registered a total of {len(people)} people")

print(
    f"The highest weight you entered was {highestWeight[0]:.2f}, and the people who have that weight were: ", end='')
for person in range(1, len(highestWeight)):
    print(highestWeight[person], end=' ')
    
print(
    f"\n The lowest weight you entered was {lowestWeight[0]:.2f}, and the people who have that weight were: ", end='')
for person in range(1, len(lowestWeight)):
    print(lowestWeight[person], end=' ')  