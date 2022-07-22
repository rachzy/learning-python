values = []
odds = []
even = []

choice = ""
while choice != "N":
    values.append(int(input("Enter a number: ")))
    choice = str(input("Wanna keep entering values? [Y/N] ")).upper()

for n in values:
    if(n % 2 == 0):
        even.append(n)
    else:
        odds.append(n)

print(f"You entered the values: {sorted(values)}")
print(f"The even values you entered were: {sorted(even)}")
print(f"The odd values you entered were: {sorted(odds)}")