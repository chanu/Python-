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

# Function to write data to a file
def write_data_to_file(filename, organizations):
    try:
        with open(filename, 'w') as file:
            for organization in organizations:
                for employee in organization.employees:
                    file.write(f"{organization.name},{organization.location},{organization.industry},"
                               f"{employee.name},{employee.position}\n")

        print(f"Data written to '{filename}' successfully.")

    except Exception as e:
        print(f"An unexpected error occurred while writing to the file: {e}")

# Function to read data from a file and create objects
def read_data_from_file(filename):
    organizations = []

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            for line in lines:
                data = line.strip().split(',')
                name, location, industry, employee_name, position = data

                if not any(org.name == name for org in organizations):
                    organization = Organization(name, location, industry)
                    organizations.append(organization)
                else:
                    organization = next(org for org in organizations if org.name == name)

                employee = Employee(employee_name, position, organization)
                organization.add_employee(employee)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading from the file: {e}")

    return organizations

# Dynamic Code
organizations = []

while True:
    print("\n1. Create Organization")
    print("2. Create Employee")
    print("3. Establish Relationship")
    print("4. Write Data to File")
    print("5. Read Data from File")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter organization name: ")
        location = input("Enter organization location: ")
        industry = input("Enter organization industry: ")
        organization = Organization(name, location, industry)
        organizations.append(organization)
        print(f"Organization '{name}' created.")

    elif choice == '2':
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        org_name = input("Enter organization name for the employee: ")

        try:
            organization = next(org for org in organizations if org.name == org_name)
            employee = Employee(name, position, organization)
            organization.add_employee(employee)
            print(f"Employee '{name}' created and added to '{org_name}'.")
        except StopIteration:
            print(f"Error: Organization '{org_name}' not found.")

    elif choice == '3':
        org_name = input("Enter organization name: ")
        emp_name = input("Enter employee name: ")

        try:
            organization = next(org for org in organizations if org.name == org_name)
            employee = next(emp for emp in organization.employees if emp.name == emp_name)
            print(f"Relationship established between '{org_name}' and '{emp_name}'.")
        except StopIteration:
            print(f"Error: Organization '{org_name}' or Employee '{emp_name}' not found.")

    elif choice == '4':
        file_path = input("Enter file path to write data: ")
        write_data_to_file(file_path, organizations)

    elif choice == '5':
        file_path = input("Enter file path to read data: ")
        read_organizations = read_data_from_file(file_path)

        for i, organization in enumerate(read_organizations):
            print(f"\nOrganization {i + 1}:")
            print("Name:", organization.name)
            print("Location:", organization.location)
            print("Industry:", organization.industry)
            print("Employees:")
            for j, employee in enumerate(organization.employees):
                print(f"  {j + 1}. Name: {employee.name}, Position: {employee.position}")

    elif choice == '6':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
