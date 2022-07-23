matrix = [[], [], []]

for i in range(3):
    for j in range(3):
        num = int(input(f"Enter a value for [{i}, {j}] "))
        matrix[i].append(num)

print("=-" * 20)

sumOfEven = sumOfThirdColumn = 0
highestValueOnSecondLine = max(matrix[1])
for i in range(3):
    for j in range(3):
        val = matrix[i][j]

        if(val % 2 == 0):
            sumOfEven += val
        if(j == 2):
            sumOfThirdColumn += val

        print(f"[ {val} ]", end=' ')
    print("\n")

print("=-" * 20)
print(f"The sum of all even values entered is equal to: {sumOfEven}")
print(f"The sum of every value in third column is equal to: {sumOfThirdColumn}")
print(f"The highest value in second line is: {highestValueOnSecondLine}")
