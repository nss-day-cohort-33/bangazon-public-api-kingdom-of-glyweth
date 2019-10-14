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

1. Please visit https://github.com/nss-day-cohort-33/bangazon-client-application-kingdom-of-glyweth to for client side instructions
2. Clone down this repository and cd into it.
3. Create your virtual environment:
```
python -m venv bangazonenv
source ./bangazonenv/bin/activate
```
4. Install the app's dependencies:
```
pip install -r requirements.txt
```

5. Now cd into bangazon_api and build your database from the existing models:
```
python manage.py makemigrations bangazon
python manage.py migrate
```

6. Populate your database with initial data from fixtures files:
```
python manage.py loaddata customer
python manage.py loaddata {etc..}
```

7. Fire up that server!
```
python manage.py runserver
```

### Authors

* **Joe Kennerly**
* **Melanie Bond**
* **Berkley Platte**
* **Ben Parker**
* **Sydney Noh**

## Acknowledgments

https://youtu.be/1TO48Cnl66w?t=70
