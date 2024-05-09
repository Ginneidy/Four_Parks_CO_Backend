from rest_framework import viewsets
from API.models.cityModel import City
from API.serializers.citySerializer import CitySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
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