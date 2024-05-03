from rest_framework import viewsets
from API.models.scheduleModel import Schedule
from API.serializers.scheduleSerializer import ScheduleSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
