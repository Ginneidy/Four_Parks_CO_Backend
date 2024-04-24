from rest_framework import serializers
from API.models.bookingModel import Booking

class BookingSerializer(serializers.ModelSerializer):
   client_name = serializers.CharField(source='client_id.name', read_only=True)
   parking_name = serializers.CharField(source='parking_id.name', read_only=True)
   vehicle_plate = serializers.CharField(source='vehicleid.plate', read_only=True)
   #reservations = BookingSerializer(many=True, read_only=True)
   def create(self, validated_data):
        # Get the related objects from the validated data
        client = validated_data.pop('client_id')
        parking_lot = validated_data.pop('parking_id')
        vehicle = validated_data.pop('vehicle_id')
        #data = {key: value for key, value in validated_data.items() if key != 'reservations'}

        # Create the parking lot instance using the related objects
        reservation = Booking.objects.create(**validated_data, client_id=client, parking_id=parking_lot, vehicle_id=vehicle)
        return reservation
 
   class Meta:
      model = Booking
      fields = ['id', 'check_in','check_out', 'client_id', 'parking_id', 'vehicle_id', 'client_name', 'parking_name', 'vehicle_plate']
