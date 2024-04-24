from rest_framework import viewsets
from API.models.parkingLotModel import ParkingLot
from API.serializers.parkingLotSerializer import ParkingLotSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.


class ParkingLotViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer
    def get_parking(self, parking_id):
        try:
            return ParkingLot.objects.get(id=parking_id)
        except ParkingLot.DoesNotExist:
            return None
    def get(self, request, parking_id, *args, **kwargs):
        parking = self.get_parking(parking_id)
        if not parking:
            return Response(
                {"res": "El parqueadero no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = ParkingLotSerializer(parking)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(detail=False, methods=['GET'], url_path="capacities", url_name="capacities")
    def capacities(self, request):
        parking_lots = self.get_queryset()  
        capacities_data = []
        for parking_lot in parking_lots:
            capacities_data.append({
            "id": parking_lot.id,
            "name": parking_lot.name,
            "current_capacity": parking_lot.get_current_capacity(),
            "total_capacity": parking_lot.spaces
        })
        return Response(capacities_data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        parkingLot = {
            "name": request.data.get("name"),
            "spaces": request.data.get("spaces"),
            "statuts": request.data.get("statuts"),
            "address": request.data.get("address"),
            "admin_id": request.user.id,
            "city_id": request.city.id,
            "parking_type_id": request.parking_type.id,
            "loyalty_id": request.loyalty.id,
        }
        serializer = ParkingLotSerializer(data=parkingLot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, parking_id, *args, **kwargs):
        parkingLot = self.get_parking(parking_id)
        if not parkingLot:
            return Response(
                {"res": "El parqueadero no existe"}, status=status.HTTP_404_NOT_FOUND
            )

        parkingLot = {
            "name": request.data.get("name"),
            "spaces": request.data.get("spaces"),
            "statuts": request.data.get("statuts"),
            "address": request.data.get("address"),
            "admin_id": request.user.id,
            "city_id": request.city.id,
            "parking_type_id": request.parking_type.id,
            "loyalty_id": request.loyalty.id,
        }
        serializer = ParkingLotSerializer(parkingLot, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, resquest, parkingLot_id, *args, **kwargs):
        parkingLot = self.get_parking(parkingLot_id)
        if not parkingLot:
            return Response(
                {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        parkingLot.delete()
        return Response({"res": "Elemento eliminado"}, status=status.HTTP_200_OK)
