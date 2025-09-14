import os
import django
import sys

# Setup Django environment
sys.path.append('c:/Users/Nihal/Desktop/coursera/module12')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dealership_project.settings')
django.setup()

from django.contrib.auth.models import User

# Create test user
if not User.objects.filter(username='testuser').exists():
    User.objects.create_user('testuser', 'test@example.com', 'testpass123')
    print("Test user 'testuser' created successfully")
else:
    print("Test user 'testuser' already exists")