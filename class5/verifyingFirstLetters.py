city = str(input("Enter the name of a city/state: \n")).strip();

if(city.upper().startswith('NEW')):
    print("This city/state starts with NEW!");
else:
    print("This city/state DOESN'T start with NEW!");

# Other way of doing it:
# if(city[:3].upper() == 'NEW'):
#     print("This city/state starts with NEW!");
# else:
#     print("This city/state DOESN'T start with NEW!");