name = str(input("Enter your name: \n")).strip();

print(f"Your name in upper is: {name.upper()}");
print(f"Your name in lower is: {name.lower()}");
print(f"Your name has {len(name) - name.count(' ')} letters");
print(f"Your first name has {name.find(' ')} letters");
