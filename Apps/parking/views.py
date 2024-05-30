from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.db import transaction
from django.http import FileResponse
from django.db.models.functions import TruncHour
from django.db.models import Count, Avg, Max, Min, DurationField, ExpressionWrapper, F

from Apps.authentication.models import Role, User
from Apps.pricing.models import Fee, Loyalty
from Apps.reservation_billing.models import Booking
from Apps.parking.models import Parking, ParkingType, City, Schedule
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
from helpers.PDF.parking_usage import generate_parking_usage_pdf


# api/parking/schedules
class ScheduleViewSet(BaseViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


# api/parking/parkings
class ParkingViewSet(BaseViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

    # [GET] api/parking/parkings/occupation/?admin_id={id}
    @action(detail=False, methods=["GET"])
    def parking_occupation(self, request):
        admin_id = request.query_params.get("admin_id")

        if not admin_id:
            return Response(
                {"error": "admin_id es requerido"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            parking = Parking.objects.get(admin_id=admin_id)
        except Parking.DoesNotExist:
            return Response(
                {"error": "Parking no encontrado para el usuario admin"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Calcular la capacidad disponible
        bookings = Booking.objects.filter(
            parking=parking, check_out__gte=datetime.now()
        )
        total_booked_spaces = bookings.count()

        if parking.spaces == 0:
            occupation_percentage = (
                0.0  # Evitar división por cero si no hay espacios en el parking
            )
        else:
            occupation_percentage = round(
                (total_booked_spaces / parking.spaces) * 100, 1
            )

        return Response(
            {"occupation_percentage": occupation_percentage},
            status=status.HTTP_200_OK,
        )

    # [POST] api/parking/parkings/parking_usage_report/
    @action(detail=False, methods=["POST"])
    def parking_usage_report(self, request):
        parking_id = request.data.get("parking_id")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")

        if not start_date or not end_date:
            return Response(
                {"error": "Both start_date and end_date are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(
                days=1
            )  # Include the entire end_date
        except ValueError:
            return Response(
                {"error": "Invalid date format. Use YYYY-MM-DD"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Número de Reservas
        total_reservas = Booking.objects.filter(
            parking_id=parking_id, check_in__range=(start_date, end_date)
        ).count()

        # Tiempo Promedio de Ocupación
        bookings = Booking.objects.filter(
            parking_id=parking_id, check_in__range=(start_date, end_date)
        )
        average_occupation_time = bookings.annotate(
            duration=ExpressionWrapper(
                F("check_out") - F("check_in"), output_field=DurationField()
            )
        ).aggregate(Avg("duration"))["duration__avg"]

        # Ocupación Máxima y Mínima
        hourly_occupations = (
            Booking.objects.filter(
                parking_id=parking_id, check_in__range=(start_date, end_date)
            )
            .annotate(hour=TruncHour("check_in"))
            .values("hour")
            .annotate(occupation=Count("id"))
        )

        if hourly_occupations.exists():
            ocupacion_maxima = hourly_occupations.aggregate(Max("occupation"))[
                "occupation__max"
            ]
            ocupacion_minima = hourly_occupations.aggregate(Min("occupation"))[
                "occupation__min"
            ]
        else:
            ocupacion_maxima = 0
            ocupacion_minima = 0

        # Detalle de cada reserva
        bookings_details = bookings.annotate(
            date=F("check_in__date"),
            duration=ExpressionWrapper(
                F("check_out") - F("check_in"), output_field=DurationField()
            ),
        ).values("date", "check_in", "check_out", "duration")

        report_data = {
            "parking_name": Parking.objects.get(id=parking_id).park_name,
            "start_date": start_date.date(),
            "end_date": (end_date - timedelta(days=1)).date(),
            "total_reservas": total_reservas,
            "average_occupation_time": average_occupation_time,
            "ocupacion_maxima": ocupacion_maxima,
            "ocupacion_minima": ocupacion_minima,
            "bookings": bookings_details,
        }

        pdf_path = generate_parking_usage_pdf(report_data)
        if not pdf_path:
            return Response(
                {"error": "Error generating PDF"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return FileResponse(
            open(pdf_path, "rb"),
            content_type="application/pdf",
            as_attachment=True,
            filename=f"reporte_parqueadero_{start_date.date()}_a_{(end_date - timedelta(days=1)).date()}.pdf",
        )

    # [GET] api/parking/parkings/admin_details/?admin_id={id}
    @action(detail=False, methods=["GET"])
    def parking_admin(self, request):
        admin_id = request.query_params.get("admin_id")
        if not admin_id:
            return Response(
                {"error": "admin_id is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            admin = User.objects.get(id=admin_id)
        except User.DoesNotExist:
            return Response(
                {"error": "Admin user does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        parking = Parking.objects.filter(admin=admin).first()
        if not parking:
            return Response(
                {"error": "No parking found for the admin user"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = ParkingSerializer(parking)
        return Response(serializer.data)

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
        with transaction.atomic():

            if isinstance(admin_data, int):
                # Fetch existing admin
                try:
                    admin = User.objects.get(pk=admin_data)
                except User.DoesNotExist:
                    return Response(
                        {"error": "Admin not found"}, status=status.HTTP_404_NOT_FOUND
                    )
            else:
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
                # Send admin password
                send_admin_password(admin_data.get("email_address"), temp_password)

            # Create parking
            parking = self.create_parking(request.data, created_date, admin)

            # Create related models
            self.create_related_models(parking, request.data, created_date)

            return Response(
                {"message": "Parqueadero creado exitosamente"},
                status=status.HTTP_201_CREATED,
            )

    # Solo para desarrollo
    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        # Check if latitude and longitude are not null
        if instance.latitude is None and instance.longitude is None:
            city = instance.city
            instance.latitude, instance.longitude = generate_random_coordinates(city.id)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

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
        # Crear modelo de lealtad si se proporcionan datos de lealtad
        if data.get("loyalty"):
            parking.loyalty = Loyalty.objects.create(
                amount_points=data["loyalty"].get("amount_points"),
                amount_per_point=data["loyalty"].get("amount_per_point"),
                created_date=created_date,
            )

        # Crear modelos de horario para cada dato de horario proporcionado
        for schedule_data in data.get("schedule", []):
            schedule = Schedule.objects.create(
                week_day=schedule_data.get("week_day"),
                opening_time=schedule_data.get("opening_time"),
                closing_time=schedule_data.get("closing_time"),
                created_date=created_date,
            )
            parking.schedule.add(schedule)

        # IDs de tarifas predeterminadas
        default_fees = {
            (1, 1): 1,
            (2, 1): 2,
            (3, 1): 3,
            (4, 1): 4,
            (1, 2): 5,
            (2, 2): 6,
            (3, 2): 7,
            (4, 2): 8,
            (1, 3): 9,
            (2, 3): 10,
            (3, 3): 11,
            (4, 3): 12,
        }

        # Crear un conjunto para verificar tarifas proporcionadas
        provided_fees = set(
            (fee["fee_type"], fee["vehicle_type"]) for fee in data.get("fee", [])
        )

        # Asignar tarifas proporcionadas o crear nuevas si no existen
        for fee_data in data.get("fee", []):
            fee_queryset = Fee.objects.filter(
                fee_type_id=fee_data["fee_type"],
                vehicle_type_id=fee_data["vehicle_type"],
                amount=fee_data["amount"],
            )
            if fee_queryset.exists():
                fee = fee_queryset.first()  # Asignar la primera tarifa encontrada
            else:
                fee = Fee.objects.create(
                    fee_type_id=fee_data["fee_type"],
                    vehicle_type_id=fee_data["vehicle_type"],
                    amount=fee_data["amount"],
                    created_date=created_date,
                )
            parking.fee.add(fee)

        # Asignar tarifas predeterminadas si no se proporcionaron
        for key, fee_id in default_fees.items():
            if key not in provided_fees:
                fee = Fee.objects.get(id=fee_id)
                parking.fee.add(fee)

        parking.save()


class ParkingTypeViewSet(BaseViewSet):
    queryset = ParkingType.objects.all()
    serializer_class = ParkingTypeSerializer


class CityViewSet(BaseViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
