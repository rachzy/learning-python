values = []
choice = ""

while choice != "N":
    num = int(input("Enter a value: "))
    if num in values:
        print("Duplicated value! I ain't adding it!")
    else:
        values.append(num)
        choice = str(input("Value successfully added! Wanna enter another one? [Y/N] ")).upper()

print("=-" * 30)
print(f"You entered the values: {sorted(values)}")