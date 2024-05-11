from rest_framework import viewsets
from Apps.parking.models import Parking, ParkingType, City , Schedule
from Apps.pricing.models import Fee, Loyalty
from Apps.reservation_billing.models import Booking
from Apps.parking.serializers import ParkingSerializer, ParkingTypeSerializer, CitySerializer, ScheduleSerializer
#from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from datetime import datetime


"""@action(detail=False, methods=['GET'], url_path="capacities", url_name="capacities")
    def capacities(self, request):
        parking_lots = self.get_queryset()  
        capacities_data = []
        for parking_lot in parking_lots:
            capacities_data.append({
            "id": parking_lot.id,
            "Parking name": parking_lot.name,
            "current_capacity": parking_lot.get_current_capacity(),
            "total_capacity": parking_lot.spaces
        })
        return Response(capacities_data, status=status.HTTP_200_OK)"""
   
class ScheduleViewSet(viewsets.ModelViewSet):
   queryset = Schedule.objects.all()
   serializer_class = ScheduleSerializer   
   def get_schedule(self, schedule_id):
      try:
         return Schedule.objects.get(id=schedule_id)
      except Schedule.DoesNotExist:
         return None
   
   def get(self, request, schedule_id, *args, **kwargs):
      schedule = self.get_schedule(schedule_id)
      if not schedule:
         return Response(
            {"res" : "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
         )
      serializer = ScheduleSerializer(schedule)
      return Response(serializer.data, status=status.HTTP_200_OK)    
   
def post(self, request, *args, **kwargs):
   schedule = {
      "week_day": request.data.get("week_day"),
      "opening_time": request.data.get("opening_time"),
      "closing_time": request.data.get("closing_time")
   }
   serializer = ScheduleSerializer(data=schedule)
   if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
def put(self, request, schedule_id, *args, **kwargs):
   schedule = self.get_schedule(schedule_id)
   if not schedule:
      return Response(
         {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
      )
   schedule = {
      "week_day": request.data.get("week_day"),
      "opening_time": request.data.get("opening_time"),
      "closing_time": request.data.get("closing_time")
   }
   serializer = ScheduleSerializer(schedule, data=request.data, partial=True)
   if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete (self, request, schedule_id, *args, **kwargs):
   schedule = self.get_schedule(schedule_id)
   if not schedule:
      return Response(
         {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
      )
   schedule.delete()
   return Response({"res": "Elemento eliminado"}, status=status.HTTP_200_OK)

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    def get_parking(self, parking_id):
        try:
            return Parking.objects.get(id=parking_id)
        except Parking.DoesNotExist:
            return None
    def get(self, request, parking_id, *args, **kwargs):
        parking = self.get_parking(parking_id)
        if not parking:
            return Response(
                {"res": "El parqueadero no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = ParkingSerializer(parking)
        available_capacity = self.get_available_capacity(parking)

        serializer = ParkingSerializer(parking)
        data = serializer.data
        data['available_capacity'] = available_capacity
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    def get_available_capacity(self, parking):
        active_bookings = Booking.objects.filter(
        parking=parking,
        check_in__lte=datetime.now(),
        check_out__isnull=True
    ).count()
        available_capacity = parking.spaces - active_bookings
        return available_capacity


    def post(self, request, *args, **kwargs):
      data = request.data.copy()
      admin = request.user
      city = City.objects.get(name=data.get('city_name'))
      parking_type = ParkingType.objects.get(name=data.get('parking_type_name'))
      loyalty = Loyalty.objects.get(id=data.get('loyalty_id')) if data.get('loyalty_id') else None
      schedules = Schedule.objects.filter(id__in=data.get('schedule_ids', []))
      fees = Fee.objects.filter(id__in=data.get('fee_codes', []))
      Parking = {
            "park_name": data.get('park_name'),
            "spaces": data.get('spaces'),
            "street_address": data.get('street_address'),
            "admin": admin.user_name,
            "city": city.name,
            "parking_type": parking_type.name,
            "loyalty": loyalty.id if loyalty else None,
            "schedule": [schedule.id for schedule in schedules],
            "fee": [fee.id for fee in fees]
      }
      serializer = ParkingSerializer(data=Parking)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, parking_id, *args, **kwargs):
      Parking = self.get_parking(parking_id)
      if not Parking:
            return Response(
               {"res": "El parqueadero no existe"}, status=status.HTTP_404_NOT_FOUND
            )
      data = request.data.copy()
      admin = request.user
      city = City.objects.get(name=data.get('city_name'))
      parking_type = ParkingType.objects.get(name=data.get('parking_type_name'))
      loyalty = Loyalty.objects.get(id=data.get('loyalty_id')) if data.get('loyalty_id') else None
      schedules = Schedule.objects.filter(id__in=data.get('schedule_ids', []))
      fees = Fee.objects.filter(id__in=data.get('fee_codes', []))
      Parking = {
            "park_name": data.get('park_name'),
            "spaces": data.get('spaces'),
            "street_address": data.get('street_address'),
            "admin": admin.user_name,
            "city": city.name,
            "parking_type": parking_type.name,
            "loyalty": loyalty.id if loyalty else None,
            "schedule": [schedule.id for schedule in schedules],
            "fee": [fee.id for fee in fees]
      }
      serializer = ParkingSerializer(Parking, data=request.data, partial=True)
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, resquest, Parking_id, *args, **kwargs):
      Parking = self.get_parking(Parking_id)
      if not Parking:
            return Response(
               {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
      Parking.delete()
      return Response({"res": "Elemento eliminado"}, status=status.HTTP_200_OK)
# Create your views here.
class ParkingTypeViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = ParkingType.objects.all()
    serializer_class = ParkingTypeSerializer
    def get_ParkingType(self, ParkingType_id):
        try:
            return ParkingType.objects.get(id=ParkingType_id)
        except ParkingType.DoesNotExist:
            return None

    def get(self, request, ParkingType_id, *args, **kwargs):
        parkingType = self.get_ParkingType(ParkingType_id)
        if not parkingType:
            return Response(
                {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = ParkingTypeSerializer(parkingType)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        parkingType = {
            "description": request.data.get("description"),
        }
        serializer = ParkingTypeSerializer(data=parkingType)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, ParkingType_id, *args, **kwargs):
        parkingType = self.get_ParkingType(ParkingType_id)
        if not parkingType:
            return Response(
                {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        parkingType = {
            "description": request.data.get("description"),
            }
        serializer = ParkingTypeSerializer(parkingType, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, resquest, ParkingType_id, *args, **kwargs):
        parkingType = self.get_ParkingType(ParkingType_id)
        if not parkingType:
            return Response(
                {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        parkingType.delete()
        return Response({"res": "Elemento eliminado"}, status=status.HTTP_200_OK)
class CityViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer
    def get_City(self, city_id):
        try:
            return City.objects.get(id=city_id)
        except City.DoesNotExist:
            return None

    def get(self, request, city_id, *args, **kwargs):
        city = self.get_City(city_id)
        if not city:
            return Response(
                {"res": "La ciudad no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = CitySerializer(city)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        city = {
            "name": request.data.get("name"),
        }
        serializer = CitySerializer(data=city)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, city_id, *args, **kwargs):
        city = self.get_city(city_id)
        if not city:
            return Response(
                {"res": "La ciudad no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        city = {
            "name": request.data.get("name"),
            }
        serializer = CitySerializer(city, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, resquest, city_id, *args, **kwargs):
        city = self.get_City(city_id)
        if not city:
            return Response(
                {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        city.delete()
        return Response({"res": "Elemento eliminado"}, status=status.HTTP_200_OK)
