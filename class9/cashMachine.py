amount = float(input("How much money you wanna get? \nUS$ "))
u = amount // 1 % 10
d = amount // 10 % 10
h = amount // 100 % 10
t = amount // 1000 % 10

amountOf50 = (h * 2) + (t * 20)
amountOf20 = d // 2
amountOf10 = d % 2
amountOf1 = u

print(f"Amount of US$ 50.00 banknotes: {amountOf50:.0f}")
print(f"Amount of US$ 20.00 banknotes: {amountOf20:.0f}")
print(f"Amount of US$ 10.00 banknotes: {amountOf10:.0f}")
print(f"Amount of US$ 1.00 banknotes: {amountOf1:.0f}")
