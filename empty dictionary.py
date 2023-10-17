# Define an empty dictionary to store student data (roll number as the key)
student_data = {}

# Function to add a new student
def add_student(roll_number, name, marks):
    student_data[roll_number] = {'Name': name, 'Marks': marks}

# Function to display a student's data by roll number
def display_student(roll_number):
    student = student_data.get(roll_number)
    if student:
        print(f"Roll Number: {roll_number}")
        print(f"Name: {student['Name']}")
        print(f"Marks: {student['Marks']}")
    else:
        print("Student not found.")

# Function to list all students
def list_students():
    if student_data:
        for roll_number, student in student_data.items():
            print(f"Roll Number: {roll_number}")
            print(f"Name: {student['Name']}")
            print(f"Marks: {student['Marks']}")
    else:
        print("No students in the database.")

# Main program loop
while True:
    print("Options:")
    print("1. Add a new student")
    print("2. Display a student's data")
    print("3. List all students")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        roll_number = input("Enter student's roll number: ")
        name = input("Enter student's name: ")
        marks = float(input("Enter student's marks: "))
        add_student(roll_number, name, marks)
    elif choice == '2':
        roll_number = input("Enter student's roll number to display: ")
        display_student(roll_number)
    elif choice == '3':
        list_students()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

