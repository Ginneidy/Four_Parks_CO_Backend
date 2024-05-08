from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Parking
from .serializers import ParkingSerializer

class ParkingViewSet(viewsets.ViewSet):
    """
    A simple viewset for view all the parkings
    """
    
    queryset = Parking.objects.all()
    
    def list(self, request):
        serializer = ParkingSerializer(self.queryset, many = True)
        return Response(serializer.data)


