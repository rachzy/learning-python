weight = float(input("What's your weight? (in kg) \n"));
height = float(input("What's your height? (in meters) \n"));
bmi = weight / pow(height, 2);

print(f"Your BMI is equal to: {bmi:.2f}");
if(bmi < 18.5):
    print("You're currently UNDERWEIGHT");
elif(18.5 <= bmi < 25):
    print("You have an IDEAL WEIGHT");
elif(25 <= bmi < 30):
    print("You're currently OVERWEIGHT");
else:
    print("Bro... look for a doctor before you have a heart attack");