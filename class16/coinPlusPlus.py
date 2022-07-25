from utils import coinManager

price = float(input("Enter a price: US$ "))
print(
    f"The half of {coinManager.coin(price)} is {coinManager.half(price, False)}")
print(
    f"The double of {coinManager.coin(price)} is {coinManager.double(price, True)}")
print(f"Adding 10%, we have {coinManager.add(price, 10, True)}")
print(f"Reducing 13%, we have {coinManager.reduce(price, 13, True)}")
