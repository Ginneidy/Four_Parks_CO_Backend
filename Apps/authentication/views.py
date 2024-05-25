import hashlib
import random
import string
import re

from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction

from .models import User, Role
from .serializers import UserSerializer
from Apps.baseViewSet import BaseViewSet

from helpers.helpers import validate_full_name, validate_email
from helpers.emailHelpers import send_activation_mail


# Function for user password hashing
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# ViewSet for User operations
class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Action to handle user login
    # /api/auth/users/login/
    @action(detail=False, methods=["POST"])
    def login(self, request, *args, **kwargs):
        email_address = request.data.get("email_address")
        user_password = request.data.get("user_password")

        # Encrypt the user-provided password with MD5
        user_password_md5 = hash_password(user_password)

        user = User.objects.filter(email_address=email_address)

        if user.exists():
            # Check if the provided password matches the one stored in the database
            if user_password_md5 == user.first().user_password:
                userData = UserSerializer(user.first()).data
                return Response(userData, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"error": "Contraseña incorrecta"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {
                    "error": "No existe ningún usuario con esa dirección de correo electrónico"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    # Action to handle user registration
    # /api/auth/users/register/
    @action(detail=False, methods=["POST"])
    def register(self, request):
        data = request.data

        # Validation of required fields
        required_fields = [
            "user_name",
            "last_name",
            "email_address",
            "user_document",
            "document_type",
            "user_password",
        ]
        for field in required_fields:
            if not data.get(field):
                return Response(
                    {"error": f"{field.replace('_', ' ').capitalize()} is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if not validate_full_name(data):
            Response(
                {"error": "Nombre de usuario o apellido no válido"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validation of email
        email = data.get("email_address")
        if not validate_email(email):
            return Response(
                {"error": "Dirección de correo electrónico no válida"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validation of document type and number
        document_type = data.get("document_type")
        user_document = data.get("user_document")

        if document_type not in ["CC", "DNI", "Passport"]:
            return Response(
                {"error": "Tipo de documento no válido"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not re.match(r"^[0-9]+$", user_document):
            return Response(
                {"error": "Número de documento no válido"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validation of password
        password = data.get("user_password")

        if not password:
            return Response(
                {"error": "se requiere contraseña"}, status=status.HTTP_400_BAD_REQUEST
            )
        if not (
            any(char.isdigit() for char in password)
            and any(char.islower() for char in password)
            and any(char.isupper() for char in password)
        ):
            return Response(
                {
                    "error": "La contraseña debe contener al menos un número, una letra mayúscula y una letra minúscula."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Encrypting the password
        hashed_password = hash_password(password)

        # Activation code generation
        activation_code = "".join(
            random.choices(string.ascii_letters + string.digits, k=5)
        )

        # User creation
        created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")

        with transaction.atomic():
            serializer = UserSerializer(
                data={
                    "user_name": data.get("user_name"),
                    "last_name": data.get("last_name"),
                    "email_address": data.get("email_address"),
                    "user_password": hashed_password,
                    "document_type": data.get("document_type"),
                    "user_document": data.get("user_document"),
                    "user_token": activation_code,
                    "created_date": created_date,
                }
            )

            if serializer.is_valid():
                user = serializer.save()

                # Assigning the role
                role_id = int(
                    data.get("role", 1)
                )  # If the value is not present, 1 is assigned as the default value
                role = Role.objects.get(pk=role_id)
                user.role.add(role)

                # Sending activation email
                send_activation_mail(user.email_address, activation_code)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Action to create an admin user, haciendose
    @action(detail=False, methods=["POST"])
    def create_admin(self, request):
        data = request.data

        required_fields = {
            "user_name",
            "last_name",
            "email_address",
            "document_type",
            "user_document",
        }

        for field in required_fields:
            if not data.get(field):
                return Response(
                    {"error": f"{field.replace('_',' ').capitalize()} is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

    # Action to verify user account
    # /api/auth/users/verify_account/
    @action(detail=False, methods=["PUT"])
    def verify_account(self, request):
        user_id = request.data.get("id")
        user_token = request.data.get("user_token")
        # atomic
        try:
            user = User.objects.get(id=user_id)
            if user.user_token == user_token:
                user.user_token = None
                user.save()
                return Response(
                    "Cuenta verificada exitosamente", status=status.HTTP_200_OK
                )
            else:
                return Response(
                    "código de activación inválido", status=status.HTTP_400_BAD_REQUEST
                )
        except User.DoesNotExist:
            return Response("El usuario no existe", status=status.HTTP_404_NOT_FOUND)
