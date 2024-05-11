from rest_framework import serializers
from .models import Vehicle, VehicleType

class vehicleTypeSerializer(serializers.ModelSerializer):
   class Meta:
      model = VehicleType
      fields = '__all__'
   
class vehicleSerializer(serializers.ModelSerializer):
   class Meta:
      model = Vehicle
      fields = ['id','plate','vehicle_type']
