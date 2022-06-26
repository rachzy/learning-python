from random import shuffle;

student1 = str(input("Enter the name of the first student: \n"));
student2 = str(input("Enter the name of the second student: \n"));
student3 = str(input("Enter the name of the third student: \n"));
student4 = str(input("Enter the name of the forth student: \n"));

students = [student1, student2, student3, student4];
shuffle(students);

print(f"The order of the students that will present the work is: \n {students}")