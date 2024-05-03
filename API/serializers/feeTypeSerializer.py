from rest_framework import serializers
from API.models.feeTypeModel import FeeType

class FeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeType
        fields = '__all__'