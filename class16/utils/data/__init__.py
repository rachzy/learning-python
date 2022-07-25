from utils.coinManager import info


def readCoin(title):
    value = input(title).strip().replace(',', '.')
    while not value.replace('.', '').isdigit():
        print("ERROR! Enter a valid number!")
        value = input(title).strip()
    info(float(value))
