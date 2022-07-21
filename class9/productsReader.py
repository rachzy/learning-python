finalCost = amountOfProductsThatCostMoreThan1K = 0
cheapestProduct = 0

while True:
    productName = str(input("Enter the product name: \n"))
    productPrice = float(input("Enter the product price: \nUS$ "))

    finalCost += productPrice

    if(productPrice > 1000):
        amountOfProductsThatCostMoreThan1K += 1

    if(cheapestProduct == 0 or cheapestProduct[1] > productPrice):
        cheapestProduct = [productName, productPrice]

    choice = ""
    while (choice != "Y" and choice != "N"):
        choice = str(input("Do you wanna keep entering products? (Y/N)")).upper()
    
    if(choice == "N"):
        break
print(f"The final cost of your purchase will be US$ {finalCost:.2f}")
print(f"Tne amount of products that costs more than US$ 1000.00 is {amountOfProductsThatCostMoreThan1K}")
print(f"The cheapest product you bought was {cheapestProduct[0]} that costs US$ {cheapestProduct[1]:.2f}")