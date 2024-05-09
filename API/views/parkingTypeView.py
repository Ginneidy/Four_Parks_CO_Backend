from rest_framework import viewsets
from API.models.parkingTypeModel import ParkingType
from API.serializers.parkingTypeSerializer import ParkingTypeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class ParkingTypeViewSet(viewsets.ModelViewSet):
    
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