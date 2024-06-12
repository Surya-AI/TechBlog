@ echo off
echo The devlopment server will start in a few seconds...
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 3000
