import re

from rest_framework.response import Response
from rest_framework import status

from .get_helpers import get_current_datetime


# Function for validating credit card
def validate_credit_card(data):
    # Perform credit card validations here
    card_number = data.get("card_number")
    expiration_date = data.get("expiration_date")
    cvv = data.get("cvv")
    cardholder_name = data.get("cardholder_name")

    # Validate credit card number length
    if len(card_number) < 13 or len(card_number) > 19:
        return False

    # Validate cardholder name not empty
    if not cardholder_name:
        return False

    # Validate expiration date is not in the past
    if expiration_date < get_current_datetime():
        return False

    # Validate CVV length
    if len(str(cvv)) != 3 and len(str(cvv)) != 4:
        return False

    return True


def validate_full_name(data):
    # Validation of name and last name
    name_regex = r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?:\s+[A-Za-zÀ-ÖØ-öø-ÿ]+)*$"
    print(data.get("last_name"))
    if not (
        re.match(name_regex, data.get("user_name"))
        and re.match(name_regex, data.get("last_name"))
    ):
        return False
    return True


# Function for validating email
def validate_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)


def validate_user_data(data, required_fields):
    """
    Validates the provided admin data.

    Args:
        admin_data (dict): A dictionary containing the admin data.
        required_fields (list): A list of required fields for validation.

    Returns:
        None: If the admin data is valid.

    Raises:
        Response: If any validation error occurs, a Response object with the error message and status code is returned.
    """
    # Check if all required fields are present
    for field in required_fields:
        if not data.get(field):
            return Response(
                {"error": f"{field.replace('_', ' ').capitalize()} es requerido"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    # Validate the full name of the admin
    if not validate_full_name(data):
        return Response(
            {"error": "Nombre o apellido no válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Validate the email address of the admin
    if not validate_email(data.get("email_address")):
        return Response(
            {"error": "Dirección de correo electrónico no válida"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Validate the document type of the admin
    if data.get("document_type") not in ["CC", "DNI", "Passport"]:
        return Response(
            {"error": "Tipo de documento no válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Validate the user document of the admin
    if not re.match(r"^[0-9]+$", data.get("user_document")):
        return Response(
            {"error": "Número de documento no válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return None
