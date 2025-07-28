from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

def obter_lat_lon(cidade: str, estado: str):
    geolocator = Nominatim(user_agent="projeto-clima")

    try:
        local = geolocator.geocode(f"{cidade}, {estado}, Brasil")
        if local:
            return local.latitude, local.longitude
        else:
            print(f"❌ Local não encontrado: {cidade}, {estado}")
            return None, None
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"❌ Erro de geocodificação: {e}")
        return None, None
