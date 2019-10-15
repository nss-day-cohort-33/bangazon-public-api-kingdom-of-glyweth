#!/bin/bash

rm -rf bangazon/migrations
rm db.sqlite3
python manage.py makemigrations bangazon
python manage.py migrate
python manage.py loaddata auth_user
python manage.py loaddata customer
python manage.py loaddata payment
python manage.py loaddata order
python manage.py loaddata product_category
python manage.py loaddata product
python manage.py loaddata order_products