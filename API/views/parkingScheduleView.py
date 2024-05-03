from rest_framework import viewsets
from API.models.parkingScheduleModel import ParkingSchedule
from API.serializers.parkingScheduleSerializer import ParkingScheduleSerializer

class ParkingScheduleViewSet(viewsets.ModelViewSet):
    queryset = ParkingSchedule.objects.all()
    serializer_class = ParkingScheduleSerializer
