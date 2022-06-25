width = float(input("Enter the wall's width: \n"));
height = float(input("Enter the wall's height: \n"));
area = width * height;

print(f"Your wall has the dimension of {area:.0f}m^2");

ink = area / 2;
print(f"You'll need {ink:.0f} liters of ink to fully paint your wall");