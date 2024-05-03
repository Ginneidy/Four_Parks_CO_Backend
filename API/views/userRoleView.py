from rest_framework import viewsets
from API.models.userRoleModel import UserRole
from API.serializers.userRoleSerializer import UserRoleSerializer

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
