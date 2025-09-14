from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]
    
    name = models.CharField(max_length=100)
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=CAR_TYPES, default=SEDAN)
    year = models.IntegerField()
    
    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year})"
