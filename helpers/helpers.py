import re
import random
import string

from datetime import datetime


# Function for getting the current date and time
def get_current_datetime():
    """Get the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")


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


def get_random_string(length):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))
