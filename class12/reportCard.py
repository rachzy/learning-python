students = []

while True:
    print("=-" * 10)
    student = []
    grades = []
    student.append(str(input("Name: ")))
    for i in range(2):
        grades.append(float(input(f"Grade {i + 1}: ")))
    student.append(grades)
    students.append(student)
    print("=-" * 10)
    choice = str(input("Wanna keep inserting data? [Y/N] ")).upper()
    if choice == "N":
        break

print("=-" * 5, end=' ')
print("AVERAGES", end=' ')
print("=-" * 5)
print("NUM", end=' ' * 3)
print("NAME", end=' ' * 6)
print("AVERAGE")

for pos, student in enumerate(students):
    average = (student[1][0] + student[1][1]) / 2
    print(pos, end=' ' * 5)
    print(student[0], end=' ' * (10 - len(student[0])))
    print(average)

print('=-' * 25)

while True:
    studentNumber = int(input("Show the grades of which student? (999 to stop): "))
    if(studentNumber == 999):
        break
    print(f"The grades of {students[studentNumber][0]} were {students[studentNumber][1]}")
    print("=-" * 20)