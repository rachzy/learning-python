from datetime import datetime


overAge = 0
underAge = 0
for i in range(7):
    year = int(input(f"Enter the year that the person {i + 1} was born: "))
    age = datetime.today().year - year
    if(age >= 21):
        overAge += 1
    else:
        underAge += 1

print(f"[ +21 ] - {overAge} \n[ -21 ] - {underAge}")
