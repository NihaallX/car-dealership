from rest_framework import serializers
from .models import CarMake, CarModel

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
    make_name = serializers.CharField(source='make.name', read_only=True)
    
    class Meta:
        model = CarModel
        fields = '__all__'