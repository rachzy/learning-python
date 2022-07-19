age = int(input("How old are you? \n"))

if(age < 18):
    print(f"You'll have to enlist in Brazilian army in {18 - age} year(s)")
elif(age > 18):
    print(f"Your enlistment time in Brazilian army was {age - 18} year(s) ago")
else:
    print(f"OH FUCK! You gotta enlist in Brazilian army this year bro, get ready")
