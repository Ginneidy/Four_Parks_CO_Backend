from rest_framework import viewsets
from API.models.roleModel import Role
from API.serializers.roleSerializer import RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
