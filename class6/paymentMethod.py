price = float(input("What's the final price? \n"))
paymentMethod = int(input(
    "What's the payment method? \n 1- Cash \n 2- Credit Card \n 3- 2x on CC \n 4- 3x or more on CC \n"))

if(paymentMethod == 1):
    finalPrice = price * 90 / 100
elif(paymentMethod == 2):
    finalPrice = price * 95 / 100
elif(paymentMethod == 3):
    finalPrice = price
    installments = finalPrice / 2
    print(
        f"You're gonna pay US$ {finalPrice / 2:.2f} in each installment")
elif(paymentMethod == 4):
    finalPrice = price * 120 / 100
    installments = int(input("How many installments? \n"))
    print(
        f"You're gonna pay US$ {finalPrice / installments:.2f} in each installment")
else:
    print("Invalid option!");
    finalPrice = price;

print(f"The final price will be US$ {finalPrice:.2f}")