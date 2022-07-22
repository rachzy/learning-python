from random import randint


n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)

numbers = (n1, n2, n3, n4, n5)

print(f'Numbers sorted: {sorted(numbers)}')
print(f'The smallest number: {min(numbers)}')
print(f'The greatest number: {max(numbers)}')