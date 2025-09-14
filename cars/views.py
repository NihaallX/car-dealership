from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CarMake, CarModel
from .serializers import CarMakeSerializer, CarModelSerializer

class CarMakeViewSet(viewsets.ModelViewSet):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

@api_view(['GET'])
def get_cars(request):
    """Get all car makes"""
    car_makes = CarMake.objects.all()
    cars_data = []
    for make in car_makes:
        cars_data.append({
            'CarMake_id': make.id,
            'CarMake_name': make.name,
            'CarMake_description': make.description
        })
    return Response(cars_data)
