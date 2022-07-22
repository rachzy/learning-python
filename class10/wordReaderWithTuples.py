w1 = str(input("Enter a word: "))
w2 = str(input("Enter a word: "))
w3 = str(input("Enter a word: "))
w4 = str(input("Enter a word: "))

words = (w1, w2, w3, w4)

for word in words:
    print('-' * 10)
    print(f'The word {word} has the vocals:')
    for x in range(len(word)):
        if(word[x].upper() in "AEIOU"):
            print(word[x].upper(), end=' ')
    print('\n')