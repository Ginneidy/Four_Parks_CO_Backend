import requests

# URL base de la API
base_url = "http://127.0.0.1:8000/api/parking/parkings/"


# Obtener todos los parqueaderos
def get_all_parkings():
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener parqueaderos: {response.status_code}")
        return []


# Actualizar un parqueadero
def update_parking(parking_id):
    url = f"{base_url}{parking_id}/"
    response = requests.put(url)
    if response.status_code == 200:
        print(f"Parqueadero {parking_id} actualizado correctamente")
    else:
        print(f"Error al actualizar parqueadero {parking_id}: {response.status_code}")


# Script principal
def main():
    parkings = get_all_parkings()
    for parking in parkings:
        parking_id = parking["id"]
        update_parking(parking_id)


if __name__ == "__main__":
    main()
