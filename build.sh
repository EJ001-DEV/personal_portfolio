#!/bin/bash

#Build the project
echo "Building the project"
pip install virtualenv
virtualenv venv
source venv/bin/activate
python3.9 -m pip install --upgrade pip

python3.9 -m pip install -r requirements.txt


#ENV PIP_ROOT_USER_ACTION=ignore

echo "Make Migration..."

python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static"
python3.9 manage.py collectstatic --noinput --clear

#python manage.py findstatic code.png

#chmod 777 /vercel/path0/staticfiles_build/static/

#echo "Give permissions"
#chmod 777 "/vercel/path0/staticfiles_build/static/"
#chmod 777 "/vercel/path0/"

#chmod 777 "/var/"