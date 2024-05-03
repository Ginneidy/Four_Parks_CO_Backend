from rest_framework import serializers
from API.models.parkingTypeModel import ParkingType

class ParkingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingType
        fields = '__all__'