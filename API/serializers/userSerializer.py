from rest_framework import serializers
from API.models.userModel import User
class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ['name', 'last_name', 'username', 'email_address', 'password', 'document_type', 'document']

