num = int(input("Enter a number: \n"));

u = num // 1 % 10;
d = num // 10 % 10;
h = num // 100 % 10;
t = num // 1000 % 10;

print(f"This number has:");
print(f"{u} units");
print(f"{d} dozens");
print(f"{h} hundreds");
print(f"{t} thousands");