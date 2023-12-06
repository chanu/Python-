

class Person:
    def __init__(self, name):
        self.name = name

class Organization(Person):
    def __init__(self, name, location, industry):
        super().__init__(name)
        self.location = location
        self.industry = industry
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee(Person):
    def __init__(self, name, position, employer):
        super().__init__(name)
        self.position = position
        self.employer = employer

# Creating Objects
organization1 = Organization("Nani Corporation", "Hyd", "software")
organization2 = Organization("7hills Foundation", "Banglore", "Education and software technologys")

employee_chanikya = Employee("chanikya", "Software Engineer", organization1)
employee_7hills = Employee("7hills","frontend developer",organization1)
employee_jane = Employee("chanikya", "Backend developer", organization2)

# Establishing Relationships
organization1.add_employee(employee_chanikya)
organization1.add_employee(employee_7hills)
organization2.add_employee(employee_jane)


# Printing
print("Organization:", organization1.name)
print("Location:", organization1.location)
print("Industry:", organization1.industry)
print("Employees:")
for employee in organization1.employees:
    print("- ", employee.name, ":", employee.position)

print("\nOrganization:", organization2.name)
print("Location:", organization2.location)
print("Industry:", organization2.industry)
print("Employees:")
for employee in organization2.employees:
    print("- ", employee.name, ":", employee.position)
