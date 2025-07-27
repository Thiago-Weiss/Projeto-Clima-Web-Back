
from .basePath import PROCESSADOS_DIR_BASE




SUB_DIR = "index"

# download
INDEX_DIR = PROCESSADOS_DIR_BASE / SUB_DIR


# colunas dos data frames do index{ano}.parquet
ARQUIVO     = "arquivo"
ANO         = "ano"
REGIAO      = "regiao"
UF          = "uf"
ESTACAO     = "estacao"
CODIGO      = "codigo"
LATITUDE    = "latitude"
LONGITUDE   = "longitude"
ALTITUDE    = "altitude"

# Lista as colunas
INDEX_COLUNAS = [
    ARQUIVO,
    ANO,
    REGIAO,
    UF,
    ESTACAO,
    CODIGO,
    LATITUDE,
    LONGITUDE,
    ALTITUDE
]

# colunas para pesquisa de estacao usando cordenadas
DISTANCIA   = "distancia"
DIRECAO     = "direcao"
