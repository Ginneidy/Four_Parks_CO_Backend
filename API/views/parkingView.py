from rest_framework import viewsets
from API.models.parkingModel import Parking
from API.serializers.parkingSerializer import ParkingSerializer

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
