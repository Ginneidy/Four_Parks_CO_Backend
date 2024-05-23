from django.shortcuts import render

from Apps.baseViewSet import BaseViewSet
from .models import VehicleType
from .serializers import VehicleTypeSerializer


class VehicleTypeViewSet(BaseViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
