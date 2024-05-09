from rest_framework import serializers
from .models import Parking, City, ParkingType, Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = '__all__'
class ParkingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingType
        fields = '__all__'
        
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'