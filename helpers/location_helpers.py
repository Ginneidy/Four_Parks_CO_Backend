import random


def generate_random_coordinates(city_id):
    """
    Generates random latitude and longitude coordinates based on the given city ID.

    Args:
    city_id (int): The ID of the city.

    Returns:
    Tuple[float, float]: A tuple containing the generated latitude and longitude coordinates.
    """
    # Coordinates for the city centers
    city_coordinates = {
        1: (4.7110, -74.0721),  # Bogota
        2: (6.2442, -75.5812),  # Medellin
        3: (10.3910, -75.4794),  # Cartagena
        4: (3.4516, -76.5319),  # Cali
        5: (11.2408, -74.1990),  # Santa Marta
        6: (10.9685, -74.7813),  # Barranquilla
        7: (7.1193, -73.1227),  # Bucaramanga
    }

    lat_variation, lon_variation = 0.1, 0.1
    if city_id in city_coordinates:
        lat, lon = city_coordinates[city_id]
        lat += random.uniform(-lat_variation, lat_variation)
        lon += random.uniform(-lon_variation, lon_variation)
        return lat, lon
    else:
        raise ValueError("Invalid city ID")
