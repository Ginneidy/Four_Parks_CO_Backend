from rest_framework import serializers
from API.models.parkingLotModel import ParkingLot

class ParkingLotSerializer(serializers.ModelSerializer):
   class Meta:
      model = ParkingLot
      fields = ['name', 'spaces', 'statuts', 'address', 'admin_id', 'city_id', 'parking_type_id', 'loyalty_id']

