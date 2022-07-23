student = dict()

student["name"] = str(input("Name: "))
student["average"] = float(input("Average: "))

print("=-" * 20)
for k, v in student.items():
    print(f"{k}: {v}")
print("Situation: ", end='')
print("Approved" if student["average"] >= 7.0 else "Disapproved")