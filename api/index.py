import os
import sys
from pathlib import Path

# Add the parent directory to the path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'echoga_project.settings')
os.environ.setdefault('DEBUG', 'False')

# Import and configure Django
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

# Setup Django
django.setup()

# Run migrations if needed
try:
    from django.core.management.commands.migrate import Command as MigrateCommand
    from django.core.management.base import CommandError
    from django.db import connection
    
    # Check if tables exist, if not run migrations
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            if len(tables) < 5:  # If very few tables, probably need migration
                execute_from_command_line(['manage.py', 'migrate', '--run-syncdb'])
    except Exception as e:
        print(f"Migration check failed: {e}")
except Exception as e:
    print(f"Migration setup failed: {e}")

# Create WSGI application
application = get_wsgi_application()

# Vercel entry point
app = application