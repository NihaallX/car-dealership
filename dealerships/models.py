from django.db import models

class Dealership(models.Model):
    dealerId = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    long = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    short_name = models.CharField(max_length=50, null=True, blank=True)
    st = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return self.name
