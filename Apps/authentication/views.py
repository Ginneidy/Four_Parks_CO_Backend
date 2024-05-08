from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):
    """
    A simple viewset for users
    """
    
    queryset = User.objects.all()
    
    def list(self, request):
        serializer = UserSerializer(self.queryset, many = True)
        return Response(serializer.data)


