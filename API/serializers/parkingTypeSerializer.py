from rest_framework import serializers
from API.models.parkingTypeModel import Parking_type
class ParkingTypeSerializer(serializers.ModelSerializer):
   class Meta:
      model = Parking_type
      fields = ['description']