import os
import sys
from pathlib import Path

# Add the parent directory to the path to find the Django project
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'echoga_project.settings')

# Import Django and setup
import django
from django.core.wsgi import get_wsgi_application

# Configure Django
django.setup()

# Create the WSGI application
application = get_wsgi_application()

# This is the entry point for Vercel
app = application