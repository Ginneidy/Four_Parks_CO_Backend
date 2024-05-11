from rest_framework import serializers
from .models import Vehicle, VehicleType

class VehicleTypeSerializer(serializers.ModelSerializer):
   class Meta:
      model = VehicleType
      fields = '__all__'
   
class VehicleSerializer(serializers.ModelSerializer):
   class Meta:
      model = Vehicle
      fields = ['id','plate','vehicle_type']
