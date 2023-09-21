
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.marks = {}
        self.grade = None

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def calculate_grade(self):
        average_mark = sum(self.marks.values()) / len(self.marks)
        if 90 <= average_mark <= 100:
            self.grade = 'A'
        elif 80 <= average_mark < 90:
            self.grade = 'B'
        elif 70 <= average_mark < 80:
            self.grade = 'C'
        elif 60 <= average_mark < 70:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print(f"Grade: {self.grade}")


# Example usage:
student1 = Student("chanikya", "123456")
student1.add_mark("Math", 85)
student1.add_mark("Science", 92)
student1.calculate_grade()
student1.display_student_info()
