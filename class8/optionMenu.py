n1 = int(input("Enter a number: \n"))
n2 = int(input("Enter another number: \n"))
option = 0

while(option != 5):
    option = int(input(
        "\nWhat you wanna do with these numbers? \n[ 1 ] - Sum \n[ 2 ] - Multiply\n[ 3 ] - Greater \n[ 4 ] - Enter new numbers \n[ 5 ] - Quit \n"))
    if option == 1:
        print(f"The sum of {n1} + {n2} = {n1 + n2}")
    elif option == 2:
        print(f"The multiplication of {n1} x {n2} = {n1 * n2}")
    elif option == 3:
        numbArr = [n1, n2]
        print(f"The greatest number you entered was: {max(numbArr)}")
    elif option == 4:
        n1 = int(input("Enter a number: \n"))
        n2 = int(input("Enter another number: \n"))
    else:
            print("You typed an invalid option.")
print("Bye")
