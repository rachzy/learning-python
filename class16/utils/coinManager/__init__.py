def coin(value: float, withComa=True):
    if(withComa):
        finalValue = f"{value:.2f}"
        return f"US$ {finalValue.replace('.', ',')}"
    return f"US$ {value:.2f}"


def half(value, convert=False):
    if(convert):
        return coin(value / 2)
    return value / 2


def double(value, convert=False):
    if(convert):
        return coin(value * 2)
    return value * 2


def add(value, amount, convert=False):
    if(convert):
        return coin(value * (100 + amount) / 100)
    return value * (100 + amount) / 100


def reduce(value, amount, convert=False):
    if(convert):
        return coin(value * (100 - amount) / 100)
    return value * (100 - amount) / 100


def line(value=30):
    print('-' * value)


def info(value):
    line()
    print(f'         COIN MANAGER')
    line()

    print("Final price:", end=' ' * 8)
    print(coin(value, True))

    print("Price doubled:", end=' ' * 6)
    print(double(value, True))

    print("Half of the price:", end=' ' * 2)
    print(half(value, True))

    print("80% of increase:", end=' ' * 4)
    print(add(value, 80, True))

    print("35% of decrease:", end=' ' * 4)
    print(reduce(value, 35, True))
    line()
