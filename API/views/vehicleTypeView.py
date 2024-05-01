from rest_framework import viewsets
from API.models.vehicleTypeModel import VehicleType
from API.serializers.vehicleTypeSerializer import VehicleTypeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.


class VehicleTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    def get_Vehicle_Type(self, vehicle_type_id):
        try:
            return VehicleType.objects.get(id=vehicle_type_id)
        except VehicleType.DoesNotExist:
            return None

    def get(self, request, vehicle_type_id, *args, **kwargs):
        vehicle_type = self.get_Vehicle_Type(vehicle_type_id)
        if not vehicle_type:
            return Response(
                {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = VehicleTypeSerializer(vehicle_type)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        vehicle_type = {
            "description": request.data.get("description"),
        }
        serializer = VehicleTypeSerializer(data=vehicle_type)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, vehicle_type_id, *args, **kwargs):
        vehicle_type = self.get_Vehicle_Type(vehicle_type_id)
        if not vehicle_type:
            return Response(
                {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        vehicle_type = {
            "description": request.data.get("description"),
            }
        serializer = VehicleTypeSerializer(vehicle_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, resquest, vehicle_type_id, *args, **kwargs):
        vehicle_type = self.get_Vehicle_Type(vehicle_type_id)
        if not vehicle_type:
            return Response(
                {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        vehicle_type.delete()
        return Response({"res": "Elemento eliminado"}, status=status.HTTP_200_OK)
