class Student:
    def __init__(self, name, student_id, age, major, grade):
        self.personal_details = PersonalDetails(name, student_id, age)
        self.major = major
        self.grade = grade
        self.name = self.personal_details.name
        self.age = self.personal_details.age
        self.student_id = self.personal_details.student_id

    def is_adult(self):
        if self.age >= 21:
            return True
        else:
            return False

class PersonalDetails:
    def __init__(self, name, student_id, age):
        self.name = name
        self.student_id = student_id
        self.age = age
