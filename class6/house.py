price = float(input("What's the house's price? \n"))
sal = float(input("What's your salary? \n"))
years = int(
    input("In how many years you're intending to pay for this property? \n"))

installment = price / (years * 12);
minimum = sal * 30 / 100;

if(installment <= minimum):
    print("You can afford this property!")
else:
    print("Sorry, you can't afford this property :/")
