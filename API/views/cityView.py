from rest_framework import viewsets
from API.models.cityModel import City
from API.serializers.citySerializer import CitySerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer