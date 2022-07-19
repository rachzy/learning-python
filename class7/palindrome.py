sentence = str(input("Enter a sentence: \n")).replace(' ', '')

sentenceBackwards = ""
for i in range(len(sentence) - 1, -1, -1):
    sentenceBackwards += sentence[i]

print(f"The inverse of {sentence} is {sentenceBackwards}")
if(sentence == sentenceBackwards):
    print("This sentence is a palindrome")
else:
    print("This sentence ISN'T a palindrome")
