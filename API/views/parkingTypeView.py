from rest_framework import viewsets
from API.models.parkingTypeModel import ParkingType
from API.serializers.parkingTypeSerializer import ParkingTypeSerializer

class ParkingTypeViewSet(viewsets.ModelViewSet):
    queryset = ParkingType.objects.all()
    serializer_class = ParkingTypeSerializer
