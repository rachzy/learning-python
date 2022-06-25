temperatureInF = int(input("Enter the temperature in °F: \n"));
temperatureInC = (temperatureInF - 32) * 5 / 9;

print(f"{temperatureInF}°F is equal to {temperatureInC:.0f}°C");