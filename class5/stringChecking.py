sentence = str(input("Enter a sentence: \n"));

print(f"The letter 'A' appears {sentence.lower().count('a')} in this sentence");
print(f"The first letter 'A' appears in the position {sentence.lower().find('a')}");
print(f"The last letter 'A' appears in the position {sentence.lower().rfind('a')}");