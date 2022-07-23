matrix = [[], [], []]

for i in range(3):
    for j in range(3):
        num = int(input(f"Enter a value for [{i}, {j}] "))
        matrix[i].append(num)

print("=-" * 20)
for i in range(3):
    for j in range(3):
        print(f"[ {matrix[i][j]} ]", end=' ')
    print("\n")