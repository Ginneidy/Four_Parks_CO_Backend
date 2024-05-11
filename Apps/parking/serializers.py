from rest_framework import serializers
from .models import Parking, City, ParkingType, Schedule
from Apps.authentication.serializers import UserSerializer
from Apps.pricing.serializers import LoyaltySerializer, FeeSerializer

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ["week_day", "opening_time", "closing_time"]

class ParkingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingType
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["city_name"]
        

class ParkingSerializer(serializers.ModelSerializer):
    admin = UserSerializer()
    city = serializers.CharField(source='city.city_name')
    parking_type = serializers.CharField(source='parking_type.description')
    loyalty = LoyaltySerializer(allow_null = True)
    schedule = ScheduleSerializer(many=True, read_only=True)
    fee = FeeSerializer(many=True, read_only=True)
    class Meta:
        model = Parking
        fields = '__all__'
    