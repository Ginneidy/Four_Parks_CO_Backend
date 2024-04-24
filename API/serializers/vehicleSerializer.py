from rest_framework import serializers
from API.models.vehicleModel import Vehicle
class VehicleSerializer(serializers.ModelSerializer):
   class Meta:
      model = Vehicle
      fields = ['plate', 'vehicle_type_id']