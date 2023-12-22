from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

organizations = []

@app.route('/')
def index():
    return render_template('index.html', organizations=organizations)
def index_organization_by_name(org_list, org_name):
    for org in org_list:
        if org.name == org_name:
            return org
    return None

# Example usage:
# Creating organizations and adding them to the list
org1 = Organization("Company A", "City A", "Tech")
org2 = Organization("Company B", "City B", "Finance")
organizations.extend([org1, org2])

# Searching for an organization by name
searched_org_name = "Company B"
result_organization = index_organization_by_name(organizations, searched_org_name)

if result_organization:
    print(f"Organization found: {result_organization.name}")
    # Do something with the found organization
else:
    print(f"Organization with name '{searched_org_name}' not found.")


@app.route('/create_organization', methods=['POST'])
def create_organization():
    name = request.form['name']
    location = request.form['location']
    industry = request.form['industry']
    organization = Organization(name, location, industry)
    organizations.append(organization)
    return redirect(url_for('index'))
def create_organization():
    org_name = input("Enter organization name: ")
    org_location = input("Enter organization location: ")
    org_industry = input("Enter organization industry: ")

    new_organization = Organization(org_name, org_location, org_industry)
    organizations.append(new_organization)

    print(f"Organization '{org_name}' created successfully!")

# Example usage:
create_organization()

# Print the list of organizations
print("List of Organizations:")
for org in organizations:
    print(f"- {org.name}")

    try:
        org_name = input("Enter organization name: ")
        if not org_name:
            raise ValueError("Organization name cannot be empty")

        org_location = input("Enter organization location: ")
        org_industry = input("Enter organization industry: ")

        new_organization = Organization(org_name, org_location, org_industry)
        organizations.append(new_organization)

        print(f"Organization '{org_name}' created successfully!")

    except ValueError as ve:
        print(f"Error: {ve}")


@app.route('/create_employee', methods=['POST'])
def create_employee():
    name = request.form['name']
    position = request.form['position']
    org_name = request.form['org_name']

    def create_employee():
        emp_name = input("Enter employee name: ")
        emp_position = input("Enter employee position: ")

        # Ask the user to select an organization for the employee
        print("Select an organization:")
        for i, org in enumerate(organizations, start=1):
            print(f"{i}. {org.name}")

        org_choice = int(input("Enter the organization number: "))

        if 1 <= org_choice <= len(organizations):
            selected_org = organizations[org_choice - 1]
            new_employee = Employee(emp_name, emp_position, selected_org)
            selected_org.add_employee(new_employee)
            print(f"Employee '{emp_name}' added to organization '{selected_org.name}' successfully!")
        else:
            print("Invalid organization choice.")

    # Example usage:
    # Create organizations first before creating employees
    create_organization()
    create_organization()

    # Create an employee
    create_employee()

    # Print the list of organizations and their employees
    print("\nList of Organizations and Employees:")
    for org in organizations:
        print(f"\nOrganization: {org.name}")
        for emp in org.employees:
            print(f"- Employee: {emp.name}, Position: {emp.position}")

    try:
        organization = next(org for org in organizations if org.name == org_name)
        employee = Employee(name, position, organization)
        organization.add_employee(employee)
        try:
            emp_name = input("Enter employee name: ")
            if not emp_name:
                raise ValueError("Employee name cannot be empty")

            emp_position = input("Enter employee position: ")

            # Ask the user to select an organization for the employee
            print("Select an organization:")
            if not organizations:
                raise ValueError("No organizations available. Please create an organization first.")

            for i, org in enumerate(organizations, start=1):
                print(f"{i}. {org.name}")

            org_choice = int(input("Enter the organization number: "))

            if 1 <= org_choice <= len(organizations):
                selected_org = organizations[org_choice - 1]
                new_employee = Employee(emp_name, emp_position, selected_org)
                selected_org.add_employee(new_employee)
                print(f"Employee '{emp_name}' added to organization '{selected_org.name}' successfully!")
            else:
                raise ValueError("Invalid organization choice.")

        except ValueError as ve:
            print(f"Error: {ve}")

        # Example usage:
        # Create organizations first before creating employees
        create_organization()
        create_organization()

        # Create an employee
        create_employee()

        # Print the list of organizations and their employees
        print("\nList of Organizations and Employees:")
        for org in organizations:
            print(f"\nOrganization: {org.name}")
            for emp in org.employees:
                print(f"- Employee: {emp.name}, Position: {emp.position}")

    except StopIteration:
        print(f"Error: Organization '{org_name}' not found.")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)







