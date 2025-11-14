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
            
student1 = Student("Alice", "alice@school.edu", [85, 90, 78])
student2 = Student("Bob", "bob@school.edu", [88, 92, 80])
student3 = Student("Charlie", "charlie@school.edu", [90, 85, 87])

student1.add_grade(95)
student1.add_grade(89)
student2.add_grade(91)
student2.add_grade(93)
student3.add_grade(88)
student3.add_grade(92)

student1.display_info()
student2.display_info()
student3.display_info()

