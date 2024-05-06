from rest_framework import serializers
from API.models.parkingModel import Parking

class ParkingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Parking
        fields = '__all__'