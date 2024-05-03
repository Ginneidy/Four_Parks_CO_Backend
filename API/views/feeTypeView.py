from rest_framework import viewsets
from API.models.feeTypeModel import FeeType
from API.serializers.feeTypeSerializer import FeeTypeSerializer

class FeeTypeViewSet(viewsets.ModelViewSet):
    queryset = FeeType.objects.all()
    serializer_class = FeeTypeSerializer