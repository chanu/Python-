class Organization:
    def __init__(self, org_id, name, location):
        self.org_id = org_id
        self.name = name
        self.location = location
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)


class Employee:
    def __init__(self, emp_id, name, role, salary):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.salary = salary


# Dynamic Data Entry
org_id = int(input("Enter Organization ID: "))
org_name = input("Enter Organization Name: ")
org_location = input("Enter Organization Location: ")

org1 = Organization(org_id=org_id, name=org_name, location=org_location)

emp_id_1 = int(input("Enter Employee 1 ID: "))
emp_name_1 = input("Enter Employee 1 Name: ")
emp_role_1 = input("Enter Employee 1 Role: ")
#emp_salary_1 = float(input("Enter Employee 1 Salary: "))
emp_salary_1_t = input("Enter Employee 2 Salary: ")
if(emp_salary_1_t.isnumeric()):
    emp_salary_1 = float(emp_salary_1_t)
else:
    print("The data entered is not valid , enter numeric Data :")
    emp_salary_1_t = input("Enter Employee 2 Salary: ")

emp1 = Employee(emp_id=emp_id_1, name=emp_name_1, role=emp_role_1, salary=emp_salary_1)

emp_id_2 = int(input("Enter Employee 2 ID: "))
emp_name_2 = input("Enter Employee 2 Name: ")
emp_role_2 = input("Enter Employee 2 Role: ")
emp_salary_2_t = input("Enter Employee 2 Salary: ")
if(emp_salary_2_t.isnumeric()):
    emp_salary_2 = float(emp_salary_2_t)
else:
    emp_salary_2_t = input("Enter Employee 2 Salary: ")



emp2 = Employee(emp_id=emp_id_2, name=emp_name_2, role=emp_role_2, salary=emp_salary_2)

org1.add_employee(emp1)
org1.add_employee(emp2)

# Display Organization and Employees
print("Organization Details:")
print(f"Org ID: {org1.org_id}, Name: {org1.name}, Location: {org1.location}")

print("\nEmployee Details:")
for employee in org1.employees:
    print(f"Emp ID: {employee.emp_id}, Name: {employee.name}, Role: {employee.role}, Salary: {employee.salary}")






