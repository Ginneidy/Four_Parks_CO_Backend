from rest_framework import serializers
from API.models.parkingLotModel import ParkingLot
#from API.serializers.bookingSerializer import BookingSerializer

class ParkingLotSerializer(serializers.ModelSerializer):
   admin_name = serializers.CharField(source='admin_id.name', read_only=True)
   city_name = serializers.CharField(source='city_id.name', read_only=True)
   parking_type_description = serializers.CharField(source='parking_type_id.description', read_only=True)
   #reservations = BookingSerializer(many=True, read_only=True)
   def create(self, validated_data):
        # Get the related objects from the validated data
        admin = validated_data.pop('admin_id')
        city = validated_data.pop('city_id')
        parking_type = validated_data.pop('parking_type_id')
        #data = {key: value for key, value in validated_data.items() if key != 'reservations'}

        # Create the parking lot instance using the related objects
        parking_lot = ParkingLot.objects.create(**validated_data, admin_id=admin, city_id=city, parking_type_id=parking_type)
        return parking_lot
 
   class Meta:
      model = ParkingLot
      fields = ['name', 'spaces', 'statuts', 'address','admin_id', 'city_id', 'parking_type_id', 'loyalty_id','admin_name', 'city_name', 'parking_type_description']

