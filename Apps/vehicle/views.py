from Apps.baseViewSet import BaseViewSet
from .models import VehicleType, Vehicle
from .serializers import VehicleTypeSerializer, VehicleSerializer


class VehicleTypeViewSet(BaseViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer

class VehicleViewSet(BaseViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer