from rest_framework import serializers
from API.models.vehicleTypeModel import VehicleType

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'