import os
import sys
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'echoga_project.settings')

# Import and setup Django
import django
django.setup()

from django.core.wsgi import get_wsgi_application

# Create WSGI application
app = get_wsgi_application()