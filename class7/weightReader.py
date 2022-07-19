highestWeight = 0
lowestWeight = 0
for i in range(5):
    weight = float(input(f"Enter the weight of the person {i + 1} (in kg): "))
    if(highestWeight == 0 or weight > highestWeight):
        highestWeight = weight
    if(lowestWeight == 0 or weight < lowestWeight):
        lowestWeight = weight

print(
    f"The highest weight entered was {highestWeight}kg and the lowest was {lowestWeight}kg")
