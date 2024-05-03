from rest_framework import serializers
from API.models.userRoleModel import UserRole

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'