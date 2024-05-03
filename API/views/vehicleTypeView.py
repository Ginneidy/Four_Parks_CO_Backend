from rest_framework import viewsets
from API.models.vehicleTypeModel import VehicleType
from API.serializers.vehicleTypeSerializer import VehicleTypeSerializer

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
