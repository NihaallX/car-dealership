from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'dealership', 'purchase', 'car_make', 'car_model', 'sentiment')
    list_filter = ('dealership', 'purchase', 'sentiment', 'car_make')
    search_fields = ('name', 'dealership__name', 'review')
