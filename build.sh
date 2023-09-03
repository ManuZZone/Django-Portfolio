#!/bin/sh

pip install -r requirements.txt
python3 manage.py makemigrations --noinput
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py runserver 0.0.0.0:8000
exec "$@"