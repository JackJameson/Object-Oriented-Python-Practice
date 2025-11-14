import re

class Student:
        def __init__(self, name, email, grades):
            self.name = name
            self.email = email
            self.grades = grades

        def add_grade(self, grade):
            self.grades.append(grade)
            
        def average_grade(self):
            if not self.grades:
                return 0
            return sum(self.grades) / len(self.grades)
        
        def display_info(self):
            print(f"Name: {self.name}")
            print(f"Email: {self.email}")
            print(f"Grades: {self.grades}")
            print(f"Average Grade: {self.average_grade()}")
            
        def grades_tuple(self):
            return tuple(self.grades)
            
student1 = Student("Alice", "alice@school.edu", [85, 90, 78])
student2 = Student("Bob", "bob@school.edu", [88, 92, 80])
student3 = Student("Charlie", "charlie@school@.edu", [90, 85, 87])

student1.add_grade(95)
student1.add_grade(89)
student2.add_grade(91)
student2.add_grade(93)
student3.add_grade(88)
student3.add_grade(92)

student1.display_info()
student2.display_info()
student3.display_info()

student_dict = {
    "alice@school.edu": student1,
    "bob@school.edu": student2,
    "charlie@school@.edu": student3
}

def get_student_by_email(email):
    return student_dict.get(email, "Student not found.")

immutable_grades = student1.grades_tuple()

try:
    immutable_grades[0] = 100
except TypeError as e:
    print(f"Error: {e}")

def list_operations(student):
    student_list = student
    for s in student_list:
        print(f"The first grade is: {s.grades[0]} and the last grade is: {s.grades[-1]}")
        print(f"Total number of grades: {len(s.grades)}")
        removed_grade = s.grades.pop()
        print(f"Last grade {removed_grade} removed. Grades after popping the last grade: {s.grades}")
        
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
for student in student_dict.values():
    if re.match(email_pattern, student.email):
        print(f"Valid email: {student.email}")
    else:
        print(f"Invalid email: {student.email}")

grades_above_90 = 0
for student in student_dict.values():
    for grade in student.grades:
        if grade >= 90:
            grades_above_90 += 1
print(f"Total number of grades above 90: {grades_above_90}")