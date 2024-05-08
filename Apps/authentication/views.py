from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import authenticate

from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for users
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail = False, methods=['POST'])
    def login(self, request, *args, **kwargs):
        email_address = request.POST.get("email_address")
        user_password = request.POST.get("user_password")
        user = User.objects.filter(email_address=email_address, user_password=user_password)

        if user.exists():
            userData = UserSerializer(user.first()).data
            return Response(userData)
        else:
            return Response({})
    
    

