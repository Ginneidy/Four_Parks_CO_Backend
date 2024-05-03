from rest_framework import serializers
from API.models.parkingFeeModel import ParkingFee

class ParkingFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingFee
        fields = '__all__'