from flask import Flask, render_template, request, redirect, url_for
from bs4 import BeautifulSoup
import requests

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
    searched_org_name = "Company B"
    result_organization = index_organization_by_name(organizations, searched_org_name)

    if result_organization:
        return f"Organization found: {result_organization.name}"
    else:
        return f"Organization with name '{searched_org_name}' not found."


def index_organization_by_name(org_list, org_name):
    for org in org_list:
        if org.name == org_name:
            return org
    return None


def web_crawler(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Check if the response content type is HTML
        content_type = response.headers.get('Content-Type', '').lower()
        if 'text/html' not in content_type:
            raise ValueError(f"Unsupported content type: {content_type}")

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.text.strip()

        return {'success': True, 'title': title}
    except requests.exceptions.RequestException as e:
        print(f"Error during web crawling: {e}")
        return {'success': False, 'error': f"Request error: {str(e)}"}
    except Exception as e:
        print(f"Error during web crawling: {e}")
        return {'success': False, 'error': str(e)}


def create_organization_from_website(url):
    try:
        # Use the web crawler function to get information from the website
        website_title = web_crawler(url)

        if website_title:
            # Create an organization using information from the website
            new_org = Organization(website_title, "Unknown", "Unknown")
            organizations.append(new_org)
            print(f"Organization '{new_org.name}' created successfully!")
        else:
            print("Failed to create organization from the website.")

    except Exception as e:
        print(f"Error during organization creation from website: {e}")


@app.route('/create_organization_from_website', methods=['POST'])
def create_organization_from_website_route():
    url = request.form['url']

    try:
        # Use the web crawler function to get information from the website
        website_title = web_crawler(url)

        if website_title:
            # Create an organization using information from the website
            new_org = Organization(website_title, "Unknown", "Unknown")
            organizations.append(new_org)
            print(f"Organization '{new_org.name}' created successfully!")
        else:
            print("Failed to create organization from the website.")

    except Exception as e:
        print(f"Error during organization creation from website: {e}")

    return redirect(url_for('index'))

    # ... (rest of the code)
def create_organization_from_website(url):
    try:
        website_title = web_crawler(url)

        if website_title:
            new_org = Organization(website_title, "Unknown", "Unknown")
            organizations.append(new_org)
            print(f"Organization '{new_org.name}' created successfully from the website!")
            return {'success': True}
        else:
            return {'success': False, 'error': 'Failed to fetch website title.'}

    except Exception as e:
        print(f"Error during organization creation from website: {e}")
        return {'success': False, 'error': str(e)}


if __name__ == '__main__':
    app.run(debug=True)


