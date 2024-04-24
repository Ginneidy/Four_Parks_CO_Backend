from rest_framework import viewsets
from API.models.vehicleModel import Vehicle
from API.serializers.vehicleSerializer import VehicleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.


class VehicleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    def get_vehicle(self, vehicle_id):
        try:
            return Vehicle.objects.get(id=vehicle_id)
        except Vehicle.DoesNotExist:
            return None

    def get(self, request, vehicle_id, *args, **kwargs):
        vehicle = self.get_vehicle(vehicle_id)
        if not vehicle:
            return Response(
                {"res": "El vehiculo no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        vehicle = {
            "plate": request.data.get("plate"),
            "vehicle_type": request.data.get("vehicle_type"),
        }
        serializer = VehicleSerializer(data=vehicle)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, vehicle_id, *args, **kwargs):
        vehicle = self.get_vehicle(vehicle_id)
        if not vehicle:
            return Response(
                {"res": "El vehiculo no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        vehicle = {
            "plate": request.data.get("plate"),
            "vehicle_type": request.data.get("vehicle_type"),
            }
        serializer = VehicleSerializer(vehicle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, resquest, vehicle_id, *args, **kwargs):
        vehicle = self.get_vehicle(vehicle_id)
        if not vehicle:
            return Response(
                {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        vehicle.delete()
        return Response({"res": "Elemento eliminado"}, status=status.HTTP_200_OK)
