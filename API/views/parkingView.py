from rest_framework import viewsets
from API.models.parkingModel import Parking
from API.serializers.parkingSerializer import ParkingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
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
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(detail=False, methods=['GET'], url_path="capacities", url_name="capacities")
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
        return Response(capacities_data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        Parking = {
            "Parking name": request.data.get("park_name"),
            "spaces": request.data.get("spaces"),
            "strert Address": request.data.get("street_address"),
            "admin_id": request.user.id,
            "city_id": request.city.id,
            "parking_type_id": request.parking_type.id,
            "loyalty_id": request.loyalty.id,
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

        Parking = {
            "Parking name": request.data.get("park_name"),
            "spaces": request.data.get("spaces"),
            "strert Address": request.data.get("street_address"),
            "admin_id": request.user.id,
            "city_id": request.city.id,
            "parking_type_id": request.parking_type.id,
            "loyalty_id": request.loyalty.id,
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