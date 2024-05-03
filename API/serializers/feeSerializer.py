from rest_framework import serializers
from API.models.feeModel import Fee

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'