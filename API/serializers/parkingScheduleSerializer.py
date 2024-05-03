from rest_framework import serializers
from API.models.parkingScheduleModel import ParkingSchedule

class ParkingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSchedule
        fields = '__all__'