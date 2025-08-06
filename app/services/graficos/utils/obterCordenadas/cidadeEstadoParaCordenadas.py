from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from app.core.const.estadosCidades import *
import pandas as pd

def obter_lat_lon(cidade: str, estado: str):
    # abre o arquivo
    df = pd.read_parquet(PARQUET_FILE_CIDADES_ESTADOS, columns= [COLUNA_ESTADO, COLUNA_CIDADE, LATITUDE, LONGITUDE])
    # filtra por estado e cidade
    df = df[(df[COLUNA_ESTADO] == estado) & (df[COLUNA_CIDADE] == cidade)]
    if not df.empty:
        lat = df[LATITUDE].iloc[0]
        lon = df[LONGITUDE].iloc[0]
        return lat, lon


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
