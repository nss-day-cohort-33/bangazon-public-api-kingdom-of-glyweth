## Bangazon API

This is a Python/Django Web API that makes each resource in Bangazon available to application developers throughout the entire company.

The resources currently within the databases are:

1. Products
1. Product types
1. Customers
1. Orders
1. Payment types
1. Employees
1. Computers
1. Training programs
1. Departments

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Computer
* Visual Studio Code (or equivalent)

### Installing

1. Clone down this repository and cd into it.
2. Create your virtual environment:
```
python -m venv workforceenv
source ./workforceenv/bin/activate
```
3. Install the app's dependencies:
```
pip install -r requirements.txt
```

4. Now cd into bangazon_api and build your database from the existing models:
```
python manage.py makemigrations hrapp
python manage.py migrate
```

5. Populate your database with initial data from fixtures files:
```
python manage.py loaddata customers
python manage.py loaddata {etc..}
```

6. Fire up that server!
```
python manage.py runserver
```

### Authors

* **Joe Kennerly**
* **Melanie Bond**
* **Berkley Platte**
* **Ben Parker**

## Acknowledgments

https://youtu.be/1TO48Cnl66w?t=70
