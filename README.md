## Bangazon API

Built using Python, Django, and the Django REST Framework for serving data to the
[client-side application](https://github.com/nss-day-cohort-33/bangazon-client-application-kingdom-of-glyweth) via HTTP

The resources currently within the database are:

[Insert IMG of ERD]

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Requirements

* Computer
* Bash Terminal
* Python 3
* Pip
* Text editor (Visual Studio Code)

### Installing

1. Clone down this repository and cd into it.
2. Once inside this repository, cd into `bangazon_api` and open your VSCode here with
`code .`
1. Create your virtual environment
```
python -m venv bangazonenv
```
* Start virtual environment on Mac
```
source ./bangazonenv/bin/activate
```
* Start virtual environment on Windows
```
source ./bangazonenv/Scripts/activate
```
5. Run `cd ..` You should be in a directory containing `requirements.txt`
6. Install the app's dependencies:
```
pip install -r requirements.txt
```

7. **Now cd into bangazon_api** and build your database from the existing models and populate the db with date from `fixtures/`:

## `seed_db.sh`
This is our way of managing database migrations

* Set execute permissions
```
chmod -x seed_db.sh
```
* Run the script
```
./seed_db.sh
```

* Fire up that server!
```
python manage.py runserver
```

## ...Test in Postman



### Authors

* **Joe Kennerly**
* **Melanie Bond**
* **Berkley Platte**
* **Ben Parker**
* **Sydney Noh**
* **Misty DeRamus**
* **Alex Rumsey**

## Acknowledgments

https://youtu.be/1TO48Cnl66w?t=70
