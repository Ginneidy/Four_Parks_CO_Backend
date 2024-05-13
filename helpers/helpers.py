from datetime import datetime


def get_current_datetime():
    """Get the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")
