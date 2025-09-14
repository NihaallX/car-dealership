from django.contrib import admin
from .models import Dealership

@admin.register(Dealership)
class DealershipAdmin(admin.ModelAdmin):
    list_display = ('dealerId', 'name', 'city', 'state', 'zip_code')
    list_filter = ('state', 'city')
    search_fields = ('name', 'city', 'state')
