from rest_framework import serializers
from .models import User
from .models import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["description"]


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(many=True, read_only=True) 

    class Meta:
        model = User
        fields = "__all__"
        
