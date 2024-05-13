import hashlib
import random
import string
import re

from datetime import datetime
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from django.db import transaction

from .models import User, Role
from .serializers import UserSerializer
from rest_framework.decorators import action
from Apps.baseViewSet import BaseViewSet

# Function to send activation email
def send_activation_mail(email, activation_code):
    subject = "User Activation Four Parks"
    message = (
        f"Gracias por registrarte! Este es tu código de activación: {activation_code}"
    )
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)

# Function for user password hashing
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Function for validating email
def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)


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
                    {"error": "Incorrect password"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {"error": "No user exists with that email address"},
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

        # Validation of name and last name
        name_regex = r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?:\s+[A-Za-zÀ-ÖØ-öø-ÿ]+)*$"
        if not re.match(name_regex, data.get("user_name")):
            return Response(
                {"error": "Invalid user name"}, status=status.HTTP_400_BAD_REQUEST
            )
        if not re.match(name_regex, data.get("last_name")):
            return Response(
                {"error": "Invalid last name"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Validation of email
        email = data.get("email_address")
        if not is_valid_email(email):
            return Response(
                {"error": "Invalid email address"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Validation of document type and number
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

        # Validation of password
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
                    "error": "The password must contain at least one number, one uppercase letter, and one lowercase letter"
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


    # Action to verify user account
    # /api/auth/users/verify_account/
    @action(detail=False, methods=["PUT"])
    def verify_account(self, request):
        user_id = request.data.get("id")
        user_token = request.data.get("user_token")

        try:
            user = User.objects.get(id=user_id)
            if user.user_token == user_token:
                user.user_token = None
                user.save()
                return Response(
                    "Successfully verified account", status=status.HTTP_200_OK
                )
            else:
                return Response(
                    "Invalid activation code", status=status.HTTP_400_BAD_REQUEST
                )
        except User.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
