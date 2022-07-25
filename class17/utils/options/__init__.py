from time import sleep
from utils import textDisplay, file

person = dict()

def accessMenu(getOptions):
    while True:
        textDisplay.line("MAIN MENU")
        for pos, option in enumerate(getOptions):
            print(f"{pos + 1} - {option['title']}")

        try:
            option = int(input("Your option: "))
            if(option < 1 or option > 3):
                print("\033[31mERROR: Invalid option! Please try again.\033[m")
                continue

            if(option == 3):
                textDisplay.line("Leaving system... Bye! :)")
                break

            getOptions[option - 1]["exec"]()
        except (TypeError, ValueError):
            print("\033[31mERROR: Please enter a valid option! \033[m")
            continue

def showPeopleTab():
    textDisplay.line("REGISTERED PEOPLE")
    people = file.read()
    for person in people:
        print(person['name'], end=' ' * (20 - len(person['name'])))
        print(f"{person['age']} years old")
    sleep(1)

def showRegisterPersonTab():
    textDisplay.line("NEW PERSON")
    person["name"] = str(input("Name: "))
    while True:
        try:
            person["age"] = int(input("Age: "))
        except (TypeError, ValueError):
            print("\033[31mERROR: Enter an Integer value!\033[m")
            continue
        else:
            registerNewPerson = file.register(person["name"], person["age"])
            if(registerNewPerson):
                print(f"\033[92mRegister of {person['name']} successfully registered!\033[m")
            person.clear()
            break
    sleep(1)
