import os
import sys
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_dir))

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'echoga_project.settings')

# Import Django
import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application

# Configure Django
django.setup()

# Get WSGI application
app = get_wsgi_application()

# Vercel serverless function handler
def handler(event, context):
    """
    Vercel serverless function handler for Django
    """
    return app(event, context)