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
    python manage.py createsuperuser --no-input --username "$DJANGO_SUPERUSER_USERNAME" --email "$DJANGO_SUPERUSER_EMAIL"

    # Set password for superuser
    python manage.py shell <<EOF
from django.contrib.auth import get_user_model
user = get_user_model().objects.get(username="$DJANGO_SUPERUSER_USERNAME")
user.set_password("$DJANGO_SUPERUSER_PASSWORD")
user.save()
EOF
fi
