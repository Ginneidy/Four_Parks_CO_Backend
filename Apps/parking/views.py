import re
import random

from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction
from django.http import Http404

from Apps.parking.models import Parking, ParkingType, City, Schedule
from Apps.pricing.models import Fee, Loyalty
from Apps.authentication.models import Role
from Apps.authentication.serializers import UserSerializer
from .serializers import (
    ParkingSerializer,
    ParkingTypeSerializer,
    CitySerializer,
    ScheduleSerializer,
)
from Apps.baseViewSet import BaseViewSet

from helpers.helpers import (
    get_current_datetime,
    validate_full_name,
    validate_email,
    get_random_string,
)
from helpers.emailHelpers import send_admin_password


# api/parking/schedules
class ScheduleViewSet(BaseViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


# api/parking/parkings
class ParkingViewSet(BaseViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

    # TODO: Que sea segun la ciudad y no solo bogota
    @staticmethod
    def generate_random_coordinates():
        """
        Generates random latitude and longitude coordinates around Bogota.

        Returns:
            Tuple[float, float]: A tuple containing the generated latitude and longitude coordinates.
        """
        lat_bogota, lon_bogota = 4.7110, -74.0721
        lat_variation, lon_variation = 0.1, 0.1
        lat = lat_bogota + random.uniform(-lat_variation, lat_variation)
        lon = lon_bogota + random.uniform(-lon_variation, lon_variation)
        return lat, lon

    # [GET] api/parking/parkings/
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific parking instance.

        Args:
            request: The request object.
            args: Additional positional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            A Response object containing the serialized parking instance data.

        Raises:
            Http404: If the parking instance does not exist.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        available_capacity = (
            instance.spaces
            - instance.booking_set.filter(check_out__gte=datetime.now()).count()
        )
        data["available_capacity"] = available_capacity
        return Response(data)

    # [POST] api/parking/parkings/
    def create(self, request, *args, **kwargs):
        """
        Create a new parking and associated admin user.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object.

        Raises:
            None
        """
        # Extract admin data from request
        admin_data = request.data.pop("admin")
        created_date = get_current_datetime()

        # Validate admin data
        validation_error = self.validate_admin_data(admin_data)
        if validation_error:
            return validation_error

        # Generate temporary password
        temp_password = get_random_string(10)

        with transaction.atomic():
            # Create admin user
            admin_serializer = UserSerializer(
                data={
                    "user_name": admin_data.get("user_name"),
                    "last_name": admin_data.get("last_name"),
                    "email_address": admin_data.get("email_address"),
                    "user_password": temp_password,
                    "document_type": admin_data.get("document_type"),
                    "user_document": admin_data.get("user_document"),
                    "created_date": created_date,
                }
            )

            if admin_serializer.is_valid():
                admin = admin_serializer.save()
                admin.role.add(Role.objects.get(pk=2))
            else:
                return Response(
                    admin_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )

            # Create parking
            parking = self.create_parking(request.data, created_date, admin)

            # Create related models
            self.create_related_models(parking, request.data, created_date)

            # Send admin password
            send_admin_password(admin_data.get("email_address"), temp_password)

            return Response(
                {"message": "Parqueadero creado exitosamente"},
                status=status.HTTP_201_CREATED,
            )

    # [GET] api/parking/parkings/{parking_id}/reservation-data/
    @action(detail=True, methods=["GET"], url_path="reservation-data")
    def get_reservation_data(self, request, *args, **kwargs):
        """
        Get reservation data for a specific parking.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object.

        Raises:
            Http404: If the parking instance does not exist.
        """
        parking_id = kwargs.get("pk")
        try:
            parking = Parking.objects.get(pk=parking_id)
        except Parking.DoesNotExist:
            raise Http404("Parking not found")

        # Get the first schedule for the parking
        first_schedule = Schedule.objects.filter(parking=parking).first()

        # Check if the parking is open 24 hours
        is_24_hours = False
        if (
            first_schedule
            and first_schedule.opening_time == "00:00"
            and first_schedule.closing_time == "00:00"
        ):
            is_24_hours = True

        # Get the hourly rate for vehicle type 1 and 2 with fee type 1
        hourly_rates = list(
            Fee.objects.filter(
                parking=parking, fee_type_id=1, vehicle_type_id__in=[1, 2]
            ).values("vehicle_type_id", "amount")
        )

        data = {
            "is_24_hours": is_24_hours,
            "opening_time": first_schedule.opening_time if first_schedule else None,
            "closing_time": first_schedule.closing_time if first_schedule else None,
            "hourly_rates": hourly_rates,
        }

        return Response(data)

    def validate_admin_data(self, admin_data):
        """
        Validates the provided admin data.

        Args:
            admin_data (dict): A dictionary containing the admin data.

        Returns:
            None: If the admin data is valid.

        Raises:
            Response: If any validation error occurs, a Response object with the error message and status code is returned.
        """
        # Define the required fields for admin data
        required_fields = [
            "user_name",
            "last_name",
            "email_address",
            "document_type",
            "user_document",
        ]

        # Check if all required fields are present
        for field in required_fields:
            if not admin_data.get(field):
                return Response(
                    {"error": f"{field.replace('_', ' ').capitalize()} es requerido"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        print(f"admin_data: {admin_data}")
        # Validate the full name of the admin
        if not validate_full_name(admin_data):
            return Response(
                {"error": "Nombre de administrador o apellido no válido"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validate the email address of the admin
        if not validate_email(admin_data.get("email_address")):
            return Response(
                {"error": "Dirección de correo electrónico no válida"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validate the document type of the admin
        if admin_data.get("document_type") not in ["CC", "DNI", "Passport"]:
            return Response(
                {"error": "Tipo de documento no válido"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validate the user document of the admin
        if not re.match(r"^[0-9]+$", admin_data.get("user_document")):
            return Response(
                {"error": "Número de documento no válido"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return None

    def create_parking(self, data, created_date, admin):
        """
        Create a new parking object.

        Args:
            data (dict): A dictionary containing the data for the new parking object.
            created_date (datetime): The created date for the new parking object.
            admin (User): The admin user for the new parking object.

        Returns:
            Parking: The created parking object.
        """
        # Create parking object
        parking = Parking.objects.create(
            park_name=data.get("park_name"),  # Get the park name from the request data
            spaces=data.get("spaces"),  # Get the number of spaces from the request data
            street_address=data.get(
                "street_address"
            ),  # Get the street address from the request data
            parking_type_id=data.get(
                "parking_type"
            ),  # Get the parking type from the request data
            created_date=created_date,  # Set the created date
            admin=admin,  # Set the admin user
            city=City.objects.get(
                pk=data.get("city")
            ),  # Get the city object based on the city ID from the request data
        )
        # Generate random coordinates for the parking location
        parking.latitude, parking.longitude = self.generate_random_coordinates()
        parking.save()  # Save the parking object
        return parking  # Return the created parking object

    def create_related_models(self, parking, data, created_date):
        """
        Creates related models for the given parking object based on the provided data.

        Args:
            parking (Parking): The parking object for which related models are created.
            data (dict): The data containing information for creating related models.
            created_date (datetime): The created date to be set for the created models.

        Returns:
            None
        """
        # Create loyalty model if loyalty data is provided
        if data.get("loyalty"):
            parking.loyalty = Loyalty.objects.create(
                amount_points=data["loyalty"].get("amount_points"),
                amount_per_point=data["loyalty"].get("amount_per_point"),
                created_date=created_date,
            )

        # Create schedule models for each schedule data provided
        for schedule_data in data.get("schedule", []):
            Schedule.objects.create(
                parking=parking,
                week_day=schedule_data.get("week_day"),
                opening_time=schedule_data.get("opening_time"),
                closing_time=schedule_data.get("closing_time"),
                created_date=created_date,
            )

        # Create fee models for each fee data provided
        for fee_data in data.get("fee", []):
            Fee.objects.create(
                parking=parking,
                fee_type_id=fee_data.get("fee_type"),
                vehicle_type_id=fee_data.get("vehicle_type"),
                amount=fee_data.get("amount"),
                created_date=created_date,
            )


class ParkingTypeViewSet(BaseViewSet):
    queryset = ParkingType.objects.all()
    serializer_class = ParkingTypeSerializer


class CityViewSet(BaseViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
