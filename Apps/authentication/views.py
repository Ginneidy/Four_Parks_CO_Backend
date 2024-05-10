import hashlib
import random
import string
import re

from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.db import transaction
from django.contrib.auth.hashers import check_password

from .models import User, Role
from .serializers import UserSerializer
from rest_framework.decorators import action


def send_activation_mail(email, activation_code):
    subject = "Activación usuario Four Parks"
    message = (
        f"¡Gracias por registrarte! este es tu codigo de activación: {activation_code}"
    )
    send_mail(
        subject, message, "settings.EMAIL_HOST_USER", [email], fail_silently=False
    )


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for users
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["POST"])
    def login(self, request, *args, **kwargs):
        email_address = request.data.get("email_address")
        user_password = request.data.get("user_password")

        # Encriptar la contraseña proporcionada por el usuario con MD5
        user_password_md5 = hashlib.md5(user_password.encode()).hexdigest()

        user = User.objects.filter(email_address=email_address)

        if user.exists():
            # Comprobar si la contraseña proporcionada coincide con la almacenada en la base de datos
            if user_password_md5 == user.first().user_password:
                userData = UserSerializer(user.first()).data
                return Response(userData, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"error": "La constraseña es incorrecta"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {"error": "No existe un usuario con ese correo electronico"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(detail=False, methods=["POST"])
    def register(self, request):
        data = request.data

        # Validación de campos obligatorios
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

        # Validación del nombre y apellido
        name_regex = r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?:\s+[A-Za-zÀ-ÖØ-öø-ÿ]+)*$"
        if not re.match(name_regex, data.get("user_name")):
            return Response(
                {"error": "Invalid user name"}, status=status.HTTP_400_BAD_REQUEST
            )
        if not re.match(name_regex, data.get("last_name")):
            return Response(
                {"error": "Invalid last name"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Validación del email
        email = data.get("email_address")
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            return Response(
                {"error": "Invalid email address"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Validación del número de identificación y tipo de identificación
        document_type = data.get("document_type")
        user_document = data.get("user_document")
        if document_type not in ["CC", "DNI", "Passport"]:
            return Response(
                {"error": "Invalid document type"}, status=status.HTTP_400_BAD_REQUEST
            )
        if not re.match(r"^[0-9]+$", user_document):
            return Response(
                {"error": "Invalid document number"}, status=status.HTTP_400_BAD_REQUEST
            )

        # validación de la contraseña
        password = data.get("user_password")

        if not password:
            return Response(
                {"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        if not (
            any(char.isdigit() for char in password)
            and any(char.islower() for char in password)
            and any(char.isupper() for char in password)
        ):
            return Response(
                {
                    "error": "The password must contain at least one number, one uppercase letter and one lowercase letter"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # cifrado de la contraseña
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        # codigo de activación
        activation_code = "".join(
            random.choices(string.ascii_letters + string.digits, k=5)
        )
        # 37cc732827b274ea8604f343517a79fc
        # creación del usuario
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

                # Asignar el rol
                role_id = int(
                    data.get("role", 1)
                )  # Si el valor no está presente, se asigna 1 como valor predeterminado
                role = Role.objects.get(pk=role_id)
                user.role.add(role)

                # Enviar correo electrónico de activación
                send_activation_mail(user.email_address, activation_code)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
