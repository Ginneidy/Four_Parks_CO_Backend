from rest_framework import viewsets
from API.models.userModel import User
from API.serializers.userSerializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
