import os
import django
import sys
from datetime import date

# Setup Django environment
sys.path.append('c:/Users/Nihal/Desktop/coursera/module12')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dealership_project.settings')
django.setup()

from cars.models import CarMake, CarModel
from dealerships.models import Dealership
from reviews.models import Review

# Create sample car makes and models
makes_data = [
    {'name': 'Toyota', 'description': 'Japanese automotive manufacturer known for reliability'},
    {'name': 'Ford', 'description': 'American automotive company'},
    {'name': 'BMW', 'description': 'German luxury automotive manufacturer'},
    {'name': 'Honda', 'description': 'Japanese automotive manufacturer'},
    {'name': 'Chevrolet', 'description': 'American automotive division of General Motors'}
]

for make_data in makes_data:
    make, created = CarMake.objects.get_or_create(**make_data)
    if created:
        print(f"Created car make: {make.name}")

# Create sample car models
models_data = [
    {'name': 'Camry', 'make': CarMake.objects.get(name='Toyota'), 'type': 'Sedan', 'year': 2023},
    {'name': 'Prius', 'make': CarMake.objects.get(name='Toyota'), 'type': 'Sedan', 'year': 2023},
    {'name': 'F-150', 'make': CarMake.objects.get(name='Ford'), 'type': 'SUV', 'year': 2023},
    {'name': 'Mustang', 'make': CarMake.objects.get(name='Ford'), 'type': 'Sedan', 'year': 2023},
    {'name': 'X5', 'make': CarMake.objects.get(name='BMW'), 'type': 'SUV', 'year': 2023},
    {'name': '3 Series', 'make': CarMake.objects.get(name='BMW'), 'type': 'Sedan', 'year': 2023},
    {'name': 'Civic', 'make': CarMake.objects.get(name='Honda'), 'type': 'Sedan', 'year': 2023},
    {'name': 'CR-V', 'make': CarMake.objects.get(name='Honda'), 'type': 'SUV', 'year': 2023},
]

for model_data in models_data:
    model, created = CarModel.objects.get_or_create(**model_data)
    if created:
        print(f"Created car model: {model.name}")

# Create sample dealerships
dealerships_data = [
    {
        'dealerId': 1,
        'name': 'Best Cars Toyota',
        'city': 'Austin',
        'state': 'TX',
        'zip_code': '78701',
        'address': '123 Main St',
        'lat': 30.2672,
        'long': -97.7431,
        'short_name': 'Toyota Austin',
        'st': 'TX'
    },
    {
        'dealerId': 2,
        'name': 'Ford Downtown',
        'city': 'Dallas',
        'state': 'TX',
        'zip_code': '75201',
        'address': '456 Commerce St',
        'lat': 32.7767,
        'long': -96.7970,
        'short_name': 'Ford Dallas',
        'st': 'TX'
    },
    {
        'dealerId': 3,
        'name': 'BMW Luxury Motors',
        'city': 'Los Angeles',
        'state': 'CA',
        'zip_code': '90210',
        'address': '789 Rodeo Dr',
        'lat': 34.0522,
        'long': -118.2437,
        'short_name': 'BMW LA',
        'st': 'CA'
    },
    {
        'dealerId': 4,
        'name': 'Honda City',
        'city': 'Kansas City',
        'state': 'KS',
        'zip_code': '66101',
        'address': '321 Kansas Ave',
        'lat': 39.0997,
        'long': -94.5786,
        'short_name': 'Honda KC',
        'st': 'KS'
    }
]

for dealer_data in dealerships_data:
    dealer, created = Dealership.objects.get_or_create(**dealer_data)
    if created:
        print(f"Created dealership: {dealer.name}")

# Create sample reviews
reviews_data = [
    {
        'name': 'John Smith',
        'dealership': Dealership.objects.get(dealerId=1),
        'review': 'Great service and friendly staff. Highly recommend this dealership!',
        'purchase': True,
        'purchase_date': date(2023, 10, 15),
        'car_make': 'Toyota',
        'car_model': 'Camry',
        'car_year': 2023,
        'sentiment': 'positive'
    },
    {
        'name': 'Sarah Johnson',
        'dealership': Dealership.objects.get(dealerId=1),
        'review': 'Good experience overall, but the wait time was a bit long.',
        'purchase': True,
        'purchase_date': date(2023, 9, 20),
        'car_make': 'Toyota',
        'car_model': 'Prius',
        'car_year': 2023,
        'sentiment': 'neutral'
    },
    {
        'name': 'Mike Wilson',
        'dealership': Dealership.objects.get(dealerId=2),
        'review': 'Excellent customer service and great deals on Ford vehicles.',
        'purchase': True,
        'purchase_date': date(2023, 8, 5),
        'car_make': 'Ford',
        'car_model': 'F-150',
        'car_year': 2023,
        'sentiment': 'positive'
    },
    {
        'name': 'Lisa Brown',
        'dealership': Dealership.objects.get(dealerId=4),
        'review': 'Professional staff and clean facility. Very satisfied with my Honda purchase.',
        'purchase': True,
        'purchase_date': date(2023, 11, 1),
        'car_make': 'Honda',
        'car_model': 'Civic',
        'car_year': 2023,
        'sentiment': 'positive'
    }
]

for review_data in reviews_data:
    review, created = Review.objects.get_or_create(**review_data)
    if created:
        print(f"Created review by: {review.name}")

print("Sample data created successfully!")