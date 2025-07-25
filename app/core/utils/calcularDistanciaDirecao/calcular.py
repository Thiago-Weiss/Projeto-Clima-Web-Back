from math import radians, sin, cos, sqrt, atan2, degrees



def calcular_distancia_direcao(lat1, lon1, lat2, lon2):
    R = 6371  # Raio da Terra em km

    # Distância Haversine
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    distancia = R * 2 * atan2(sqrt(a), sqrt(1 - a))

    # Cálculo do ângulo/direção em graus (bearing)
    y = sin(dlon) * cos(radians(lat2))
    x = cos(radians(lat1)) * sin(radians(lat2)) - sin(radians(lat1)) * cos(radians(lat2)) * cos(dlon)
    direcao_rad = atan2(y, x)
    direcao_graus = (degrees(direcao_rad) + 360) % 360  # Normaliza para 0–360°

    return distancia, direcao_graus