from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geo_system")

def reverse_geocode(gps):
    if not gps:
        return None
    lat, lon = gps
    location = geolocator.reverse((lat, lon), zoom=18)
    return location.address if location else None
