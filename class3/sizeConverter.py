size = float(input("Enter a measurement (in meters) \n"));
sizeInCm = size * 100;
sizeInMm = size * 1000;

print(f"The measure of {size} corresponds to {sizeInCm:.0f}cm and {sizeInMm:.0f}mm");