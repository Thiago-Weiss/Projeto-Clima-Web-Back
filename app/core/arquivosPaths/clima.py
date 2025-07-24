import os
from datetime import datetime
from .basePath import DOWNLOAD_DIR_BASE, EXTRACT_DIR_BASE, PROCESSADOS_DIR_BASE


# url de download
URL_DOWNLOAD = 'https://portal.inmet.gov.br/uploads/dadoshistoricos/'


# processamento do arquivo (dir e files)
SUB_DIR = "clima"

# download
ZIP_DIR = DOWNLOAD_DIR_BASE / SUB_DIR

# extraido
EXTRACT_DIR = EXTRACT_DIR_BASE / SUB_DIR

# salvo o arquivo final
PARQUET_DIR =  PROCESSADOS_DIR_BASE / SUB_DIR



# ano dos arquivos
ANO_INICIO   = 2000
ANO_FINAL = datetime.now().year




# colunas da tabela
DATA                = "data"
HORA                = "hora"
PRECIPITACAO        = "precipitacao"
PRESSAO             = "pressao"
PRESSAO_MAX         = "pressao_max"
PRESSAO_MIN         = "pressao_min"
RADIACAO            = "radiacao"
TEMP_AR             = "temp_ar"
TEMP_ORVALHO        = "temp_orvalho"
TEMP_MAX            = "temp_max"
TEMP_MIN            = "temp_min"
ORVALHO_MAX         = "orvalho_max"
ORVALHO_MIN         = "orvalho_min"
UMIDADE_MAX         = "umidade_max"
UMIDADE_MIN         = "umidade_min"
UMIDADE             = "umidade"
VENTO_DIRECAO       = "vento_direcao"
VENTO_RAJADA        = "vento_rajada"
VENTO_VELOCIDADE    = "vento_velocidade"

# Lista com todas as colunas na ordem
COLUNAS_PADRAO = [
    DATA,
    HORA,
    PRECIPITACAO,
    PRESSAO,
    PRESSAO_MAX,
    PRESSAO_MIN,
    RADIACAO,
    TEMP_AR,
    TEMP_ORVALHO,
    TEMP_MAX,
    TEMP_MIN,
    ORVALHO_MAX,
    ORVALHO_MIN,
    UMIDADE_MAX,
    UMIDADE_MIN,
    UMIDADE,
    VENTO_DIRECAO,
    VENTO_RAJADA,
    VENTO_VELOCIDADE
]



VALOR_ALTURA_NULA = -9999

