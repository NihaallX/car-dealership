from django.db import models
from django.contrib.auth.models import User
from dealerships.models import Dealership
from cars.models import CarModel

class Review(models.Model):
    name = models.CharField(max_length=100)
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)
    review = models.TextField()
    purchase = models.BooleanField(default=False)
    purchase_date = models.DateField(null=True, blank=True)
    car_make = models.CharField(max_length=100, null=True, blank=True)
    car_model = models.CharField(max_length=100, null=True, blank=True)
    car_year = models.IntegerField(null=True, blank=True)
    sentiment = models.CharField(max_length=10, default='neutral')
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return f"Review by {self.name} for {self.dealership.name}"
