from rest_framework import viewsets
from API.models.userModel import User
from API.serializers.userSerializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_User(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def get(self, request, user_id, *args, **kwargs):
        user = self.get_User(user_id)
        if not user:
            return Response(
                {"res": "El usuario no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = {
            "name": request.data.get("name"),
            "last_name": request.data.get("last_name"),
            "username": request.data.get("username"),
            "email_address": request.data.get("email_address"),
            "password": request.data.get("password"),
            "document_type": request.data.get("document_type"),
            "document": request.data.get("document"),}
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id, *args, **kwargs):
        user = self.get_user(user_id)
        if not user:
            return Response(
                {"res": "El usuario no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        user = {
            "name": request.data.get("name"),
            "last_name": request.data.get("last_name"),
            "username": request.data.get("username"),
            "email_address": request.data.get("email_address"),
            "password": request.data.get("password"),
            "document_type": request.data.get("document_type"),
            "document": request.data.get("document"),}
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, resquest, user_id, *args, **kwargs):
        user = self.get_User(user_id)
        if not user:
            return Response(
                {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        user.delete()
        return Response({"res": "Elemento eliminado"}, status=status.HTTP_200_OK)
