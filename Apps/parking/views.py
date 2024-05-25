import re

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction

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

from helpers.get_helpers import get_current_datetime, get_random_string
from helpers.validate_helpers import validate_user_data
from helpers.email_helpers import send_admin_password
from helpers.location_helpers import generate_random_coordinates
from helpers.password_helpers import hash_password


# api/parking/schedules
class ScheduleViewSet(BaseViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


# api/parking/parkings
class ParkingViewSet(BaseViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

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
        validation_error = validate_user_data(
            admin_data,
            [
                "user_name",
                "last_name",
                "email_address",
                "document_type",
                "user_document",
            ],
        )
        if validation_error:
            return validation_error

        # Generate temporary password
        temp_password = get_random_string(10)
        hashed_password = hash_password(temp_password)

        with transaction.atomic():
            # Create admin user
            admin_serializer = UserSerializer(
                data={
                    "user_name": admin_data.get("user_name"),
                    "last_name": admin_data.get("last_name"),
                    "email_address": admin_data.get("email_address"),
                    "user_password": hashed_password,
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
        # Generate random coordinates based on the city
        city_id = data.get("city")
        parking.latitude, parking.longitude = generate_random_coordinates(city_id)
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
            schedule = Schedule.objects.create(
                week_day=schedule_data.get("week_day"),
                opening_time=schedule_data.get("opening_time"),
                closing_time=schedule_data.get("closing_time"),
                created_date=created_date,
            )
            parking.schedule.add(schedule)

        # Create fee models for each fee data provided
        for fee_data in data.get("fee", []):
            fee = Fee.objects.create(
                fee_type_id=fee_data.get("fee_type"),
                vehicle_type_id=fee_data.get("vehicle_type"),
                amount=fee_data.get("amount"),
                created_date=created_date,
            )
            parking.fee.add(fee)

        parking.save()


class ParkingTypeViewSet(BaseViewSet):
    queryset = ParkingType.objects.all()
    serializer_class = ParkingTypeSerializer


class CityViewSet(BaseViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
