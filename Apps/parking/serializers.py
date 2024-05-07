from rest_framework import serializers
from .models import Parking, City

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = "__all__"