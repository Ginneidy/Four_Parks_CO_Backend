from rest_framework import serializers
from API.models.cityModel import City
class CitySerializer(serializers.ModelSerializer):
   class Meta:
      model = City
      fields = ['name']