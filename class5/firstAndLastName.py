name = str(input("Enter your name: \n"));
nameSplit = name.split(' ');

print(f"Your first name is {nameSplit[0]}");
print(f"Your last name is: {nameSplit[len(nameSplit) - 1]}");