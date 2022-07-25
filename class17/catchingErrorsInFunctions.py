def readInt(title):
    while True:
        try:
            n = int(input(title))
        except (TypeError, ValueError):
            print("\033[31mERROR: Please, enter an integer value.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mERROR: User stopped the execution.\033[m")
            return 0
        else:
            return n


def readFloat(title):
    while True:
        try:
            n = float(input(title))
        except (TypeError, ValueError):
            print("\033[31mERROR: Please, enter an integer value.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mERROR: User stopped the execution.\033[m")
            return 0
        else:
            return n


nInt = readInt("Enter an Integer: ")
nFlt = readFloat("Enter a Float: ")
print(f"The Integer number entered was {nInt} and the Float one was {nFlt}")
