def readInt(title):
    num = input(title)
    while not num.isnumeric():
        print("ERROR! Enter a valid integer number!")
        num = input(title)
    return num


# Main
n = readInt("Enter a number: ")
print(f"You just entered the number: {n}")
