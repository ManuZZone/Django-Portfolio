#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations --noinput
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
exec "$@"