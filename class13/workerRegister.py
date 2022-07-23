from datetime import datetime
from sqlite3 import Date


person = dict()
person["name"] = str(input("Name: "))
birthYear = int(input("Year of birth: "))
person["age"] = Date.today().year - birthYear
person["ctps"] = int(input("CPTS (0: don't have one): "))
if(person["ctps"] != 0):
    person["hireYear"] = int(input("Year of hire: "))
    person["retirementAge"] = person["age"] + ((person["hireYear"] + 35) - datetime.now().year)
    person["salary"] = float(input("Salary: US$ "))

print("=-" * 20)

for k, v in person.items():
    print(f"{k}: {v}")
