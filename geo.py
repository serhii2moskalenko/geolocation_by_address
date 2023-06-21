import webbrowser

from geopy.geocoders import Nominatim


def geocode(address):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(address, language="ru")

    if location is not None:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        raise Exception("Geocoding failed. Unable to find coordinates for the given address.")

def open_map(address):
    map_url = f"https://www.openstreetmap.org/?mlat={latitude}&mlon={longitude}&zoom=15"
    webbrowser.open(map_url)


address = str(input('Введите адрес \n->'))  # Получаем интересующий нас адрес
latitude, longitude = geocode(address)
print(f"Координаты: Широта = {latitude}, Долгота = {longitude}")
open_map(address)
