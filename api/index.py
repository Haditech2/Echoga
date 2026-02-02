import os
import sys
from pathlib import Path

# Add the parent directory to Python path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'echoga_project.settings')

# Import Django
import django
from django.core.wsgi import get_wsgi_application

# Setup Django
django.setup()

# Get WSGI application
application = get_wsgi_application()

# Handler function for Vercel
def handler(event, context):
    """
    Vercel handler function
    """
    return application(event.get('environ', {}), lambda status, headers: None)

# Export for Vercel
app = application