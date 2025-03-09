#!/bin/bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Migrate database
python manage.py migrate

# Create superuser if the variable is set
if [[ $CREATE_SUPERUSER ]]; then
    python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
