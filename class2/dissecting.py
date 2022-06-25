word = input("Enter any word you want: \n");

print(f"This word's primitive type is: {type(word)}");
print(f"Is this world composed by spaces? {word.isspace()}");
print(f"Is numeric? {word.isnumeric()}");
print(f"Is alpha? {word.isalpha()}");
print(f"Is alphanumeric? {word.isalnum()}");
print(f"Is upper? {word.isupper()}");
print(f"Is lower? {word.islower()}");
print(f"Is title? {word.istitle()}");
