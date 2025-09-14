import os
import django
import sys

# Setup Django environment
sys.path.append('c:/Users/Nihal/Desktop/coursera/module12')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dealership_project.settings')
django.setup()

from django.contrib.auth.models import User

# Create superuser
if not User.objects.filter(username='root').exists():
    User.objects.create_superuser('root', 'admin@example.com', 'password')
    print("Superuser 'root' created successfully")
else:
    print("Superuser 'root' already exists")