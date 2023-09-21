python
# Define an empty list to store student data
student_data = []

# Function to calculate the grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    else:
        return 'F'

# Function to add a new student to the list
def add_student(name, marks):
    grade = calculate_grade(marks)
    student_data.append({'Name': name, 'Marks': marks, 'Grade': grade})

# Function to display all student data
def display_students():
    for student in student_data:
        print(f"Name: {student['Name']}, Marks: {student['Marks']}, Grade: {student['Grade']}")

# Main program loop
while True:
    print("Options:")
    print("1. Add a new student")
    print("2. Display all students")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        marks = float(input("Enter student marks: "))
        add_student(name, marks)
    elif choice == '2':
        display_students()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

