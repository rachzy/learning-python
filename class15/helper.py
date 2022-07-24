from time import sleep


def line(title):
    print("~" * (len(title) + 8))
    print(f"    {title}")
    print("~" * (len(title) + 8))

while True:
    line("PyHelp - HELPING SYSTEM")
    funclib = str(input("Function or Library > "))

    if(funclib == "end"):
        line("BYE")
        break

    line(f"Accessing the manual of the command '{funclib}'")
    sleep(0.5)

    help(funclib)
