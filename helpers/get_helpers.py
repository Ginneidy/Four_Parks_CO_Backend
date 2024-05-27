
import random
import string

from datetime import datetime


# Function for getting the current date and time
def get_current_datetime():
    """Get the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")


def get_random_string(length):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))
