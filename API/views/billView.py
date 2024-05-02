from rest_framework import viewsets
from API.models.billModel import Bill
from API.serializers.billSerializer import BillSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer