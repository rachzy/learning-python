from secrets import choice


values = []
choice = ""

while choice != "N":
    num = int(input("Enter a number: "))
    values.append(num)
    choice = str(input("Wanna keep inserting data? (Y/N)")).upper()

values.sort(reverse=True)

print(f"You entered a total of {len(values)} values")
print(f"The values you entered were: {values}")
print(f"Was the number 5 entered? {5 in values}")