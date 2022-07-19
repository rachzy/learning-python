side1 = int(input("What is the measurement of the first side? \n"))
side2 = int(input("What is the measurement of the second side? \n"))
side3 = int(input("What is the measurement of the third side? \n"))

if ((side1 > side2 + side3) or (side2 > side1 + side3) or (side3 > side1 + side2)):
    print("This triangle is not real")
else:
    if(side1 == side2 == side3):
        print("This triangle is EQUILATERAL")
    elif(side1 != side2 != side3 != side1):
        print("This triangle is SCALENE")
    else:
        print("This triangle is SCALENE")
