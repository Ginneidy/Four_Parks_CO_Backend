from rest_framework import viewsets
from API.models.vehicleModel import Vehicle
from API.serializers.vehicleSerializer import VehicleSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
