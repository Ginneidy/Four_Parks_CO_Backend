from rest_framework import viewsets
from API.models.pointsModel import Points
from API.serializers.pointsSerializer import PointsSerializer

class PointsViewSet(viewsets.ModelViewSet):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer
