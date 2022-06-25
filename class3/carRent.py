miles = int(input("Enter the amount of miles that you traveled with the car: \n"));
days = int(input("Enter the amount of day that you stayed with the car: \n"));
finalPrice = (miles * 0.15) + (days * 60);

print(f"The final price will be US$ {finalPrice:.2f}");