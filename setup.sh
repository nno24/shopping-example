#!/bin/bash

python3 manage.py runserver
pip3 install django==3.2 django-allauth pillow
python3 manage.py migrate
python3 manage.py loaddata categories
python3 manage.py loaddata products
