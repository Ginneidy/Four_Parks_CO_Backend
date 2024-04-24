from rest_framework import serializers
from API.models.bookingModel import Booking
class BookingSerializer(serializers.ModelSerializer):
   class Meta:
      model = Booking
      fields = ['id', 'date', 'client_name', 'parking_name', 'vehicle_plate']
