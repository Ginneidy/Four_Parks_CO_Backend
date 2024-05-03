from rest_framework import serializers
from API.models.roleModel import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'