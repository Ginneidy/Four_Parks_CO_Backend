from rest_framework import viewsets
from API.models.feeModel import Fee
from API.serializers.feeSerializer import FeeSerializer

class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer