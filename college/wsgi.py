# college/wsgi.py

import os

from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'application' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college.settings')

application = get_wsgi_application()
app = application
