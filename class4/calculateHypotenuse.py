from math import hypot

square1 = float(input("Enter the value of the 1st square: \n"));
square2 = float(input("Enter the value of the 2nd square: \n"));
hypotenuse = hypot(square1, square2);

print(f"The hypotenuse of this triangle is equal to: {hypotenuse:.02f}");