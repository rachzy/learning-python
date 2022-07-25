dbName = "database.txt"


def checkExistence(forceCreation=False):
    try:
        file = open(dbName, 'rt')
        file.close()
    except FileNotFoundError:
        if(forceCreation):
            return create()
        return False
    else:
        return True


def create():
    try:
        newFile = open(dbName, 'wt+')
        newFile.close()
    except PermissionError:
        print("\033[31mERROR: The application is not allowed to create new files. Try executing it as administrator or moving its directory to somewhere else.\033[m")
        return False
    except:
        print(
            "\033[31mAn unknown error ocurred while trying to create the database.\033[m")
        return False
    else:
        print("Database successfully created!")
        return True


def read():
    try:
        file = open(dbName, 'rt')
    except:
        print(
            "\033[31mAn error ocurred while trying to access the database file.\033[m")
    else:
        people = list()
        person = dict()
        for line in file:
            line = line.split(';')
            person["name"] = line[0]
            person["age"] = line[1].replace('\n', '')
            people.append(person.copy())
            person.clear()
        return people


def register(name, age):
    try:
        db = open(dbName, 'at')
    except:
        print(
            "\033[31mERROR: An error ocurred while trying to access the database.\033[m")
        return False
    else:
        try:
            db.writelines(f"{name};{age}\n")
        except:
            print(
                "\033[31mERROR: An error ocurred while trying register that person.\033[m")
            return False
        else:
            db.close()
            return True
