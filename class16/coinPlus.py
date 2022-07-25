from utils import coinManager

price = float(input("Enter a price: US$ "))
print(
    f"The half of {coinManager.coin(price)} is {coinManager.coin(coinManager.half(price))}")
print(
    f"The double of {coinManager.coin(price)} is {coinManager.coin(coinManager.double(price))}")
print(f"Adding 10%, we have {coinManager.coin(coinManager.add(price, 10))}")
print(
    f"Reducing 13%, we have {coinManager.coin(coinManager.reduce(price, 13))}")
