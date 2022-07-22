numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
           'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')


userNumber = int(input("Enter the number you want wrote in full: "))

while userNumber < 0 or userNumber > 20:
    print("You can only enter numbers between 0 and 20. Please try again.")
    userNumber = int(input("Enter the number you want wrote in full: "))

print(numbers[userNumber])
