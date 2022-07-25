from utils import coinManager

price = float(input("Enter a price: US$ "))
print(f"The half of US$ {price} is {coinManager.half(price)}")
print(f"The double of US$ {price} is {coinManager.double(price)}")
print(f"Adding 10%, we have US$ {coinManager.add(price, 10)}")
print(f"Reducing 13%, we have US$ {coinManager.reduce(price, 13)}")
