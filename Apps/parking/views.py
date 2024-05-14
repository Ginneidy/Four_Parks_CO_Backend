from rest_framework import viewsets, status
from rest_framework.response import Response

from datetime import datetime

from Apps.parking.models import Parking, ParkingType, City, Schedule
from Apps.pricing.models import Fee, Loyalty
from Apps.reservation_billing.models import Booking
from Apps.parking.serializers import (
    ParkingSerializer,
    ParkingTypeSerializer,
    CitySerializer,
    ScheduleSerializer,
)
from Apps.baseViewSet import BaseViewSet


# api/parking/schedules
class ScheduleViewSet(BaseViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


# api/parking/parkings
class ParkingViewSet(BaseViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

    # [GET] api/parking/parkings/
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        available_capacity = (
            instance.spaces
            - instance.booking_set.filter(check_out__gte=datetime.now()).count()
        )
        data["available_capacity"] = available_capacity
        return Response(data)
    
    

class ParkingTypeViewSet(BaseViewSet):
    queryset = ParkingType.objects.all()
    serializer_class = ParkingTypeSerializer


class CityViewSet(BaseViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
