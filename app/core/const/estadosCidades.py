from .basePath import DOWNLOAD_DIR_BASE, EXTRACT_DIR_BASE, PROCESSADOS_DIR_BASE



# url de download
# cidades do ibge
URL_DOWNLOAD_CIDADES_ESTADOS = "https://geoftp.ibge.gov.br/organizacao_do_territorio/estrutura_territorial/divisao_territorial/2024/DTB_2024.zip"
# malha municipal no site do ibge
URL_DOWNLOAD_CORDENADAS  = "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2024/Brasil/BR_Municipios_2024.zip"


# processamento do arquivo (dir e files)
SUB_DIR = "estadosCidades"

# download
ZIP_DIR = DOWNLOAD_DIR_BASE / SUB_DIR
ZIP_FILE_CIDADES_ESTADOS = ZIP_DIR / "DTB_2024.zip"
ZIP_FILE_CORDENADAS = ZIP_DIR / "BR_Municipios_2024.zip"

# extraido
EXTRACT_DIR = EXTRACT_DIR_BASE / SUB_DIR
EXTRACT_FILE_CIDADES_ESTADOS = EXTRACT_DIR / "RELATORIO_DTB_BRASIL_2024_MUNICIPIOS.ods"
EXTRACT_FILE_CORDENADAS = EXTRACT_DIR / "BR_Municipios_2024.shp"

# salvo o arquivo final
PARQUET_DIR =  PROCESSADOS_DIR_BASE / SUB_DIR
PARQUET_FILE_CIDADES_ESTADOS = PARQUET_DIR / "EstadoCidade.parquet"





# colunas do Cidade Estado
COLUNA_CIDADE = "Nome_Município"
COLUNA_ESTADO = "Nome_UF"
COLUNA_CODIGO_CIDADE = "Código Município Completo"


# colunas do Cordenadas
CENTROIDE = "centroide"
LATITUDE = "latitude"
LONGITUDE = "longitude"
CD_MUN = "CD_MUN"


