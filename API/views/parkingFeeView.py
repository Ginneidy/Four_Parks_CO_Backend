from rest_framework import viewsets
from API.models.parkingFeeModel import ParkingFee
from API.serializers.parkingFeeSerializer import ParkingFeeSerializer

class ParkingFeeViewSet(viewsets.ModelViewSet):
    queryset = ParkingFee.objects.all()
    serializer_class = ParkingFeeSerializer
