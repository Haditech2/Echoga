from django.http import HttpResponse
from django.shortcuts import render
import os
import sys
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_dir))

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'echoga_project.settings')

# Import and setup Django
import django
django.setup()

from foundation.views import home

def handler(request, context=None):
    """
    Vercel handler that serves the Django home page
    """
    try:
        # Create a mock request object for Django
        from django.test import RequestFactory
        factory = RequestFactory()
        django_request = factory.get('/')
        
        # Call the home view
        response = home(django_request)
        return response
        
    except Exception as e:
        return HttpResponse(f"""
        <html>
        <head><title>ECHOGA Foundation</title></head>
        <body>
            <h1>ECHOGA Foundation</h1>
            <p>Website is loading... Please refresh the page.</p>
            <p>Error details: {str(e)}</p>
        </body>
        </html>
        """, content_type='text/html')