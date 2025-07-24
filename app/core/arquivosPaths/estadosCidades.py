from .basePath import BASE_DIR, DATA_DIR, DOWNLOAD_DIR_BASE, EXTRACT_DIR_BASE



# url de download
URL_DOWNLOAD = "https://geoftp.ibge.gov.br/organizacao_do_territorio/estrutura_territorial/divisao_territorial/2024/DTB_2024.zip"



# processamento do arquivo (dir e files)
SUB_DIR = "estadosCidades"

# download
ZIP_DIR = DOWNLOAD_DIR_BASE / SUB_DIR
ZIP_FILE = ZIP_DIR / "DTB_2024.zip"

# extraido
EXTRACT_DIR = EXTRACT_DIR_BASE / SUB_DIR
EXTRACT_FILE = EXTRACT_DIR / "RELATORIO_DTB_BRASIL_2024_MUNICIPIOS.ods"

# salvo o arquivo final
PARQUET_DIR =  BASE_DIR / DATA_DIR / SUB_DIR
PARQUET_FILE = PARQUET_DIR / "EstadoCidade.parquet"





COLUNA_CIDADE = "Nome_Município"
COLUNA_ESTADO = "Nome_UF"







