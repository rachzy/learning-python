products = ('Hamburger', 3, 'French Fries', 2, 'Hot Dog', 3, 'Ice Cream',
            2, 'Coke', 1.5, 'Pepsi', 1.2, 'Sprite', 1.3, 'Milkshake', 3)

print('-' * 25)
print('PRODUCT LIST')
print('-' * 25)
for i in range(0, len(products), 2):
    productName = products[i]
    productPrice = products[i + 1]

    print(productName, end='')
    print('.' * (15 - len(productName)), end='')
    print(f'US$ {productPrice:.2f}')
print('_' * 25)