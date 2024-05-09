from rest_framework import serializers
from .models import Role,User


class RoleSerializer(serializers.ModelSerializer):
   class Meta:
      model = Role
      fields = '__all__'
      
class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ['user_name','last_name','email_address','document_type','user_document','role']