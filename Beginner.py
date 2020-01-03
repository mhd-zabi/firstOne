from Student import Student

student1 = Student("Zabi", "139664", 32, "BE in E&C", 3.9)
student2 = Student("Nishath", "168974", 25, "BE in IS", 4.9)
student3 = Student("Muddu", "987654", 20, "Diploma in CS", 3.1)

for student in student1, student2, student3:
    print(student.name
    + " " + str(student.age)
    + " " + student.student_id
    + " " + str(student.grade)
    + " " + student.major
    + " " + str(student.is_adult()))