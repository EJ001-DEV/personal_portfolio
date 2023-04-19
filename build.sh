#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
#pip install -m requirements.txt
#railway connect Postgres

python manage.py collectstatic --no-input
python manage.py migrate