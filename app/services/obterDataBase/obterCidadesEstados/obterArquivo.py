from os import makedirs, path
import requests
import zipfile
import pandas as pd
import geopandas as gpd

# meus arquivos
from app.core.const.estadosCidades import *


def baixarArquivoCidadesEstados():

    # garante que as pastas existem
    makedirs(ZIP_DIR, exist_ok=True)
    makedirs(EXTRACT_DIR, exist_ok=True)
    makedirs(PARQUET_DIR, exist_ok=True)

    # arquivo final
    # se nao tem o arquivo final
    if not path.exists(PARQUET_FILE_CIDADES_ESTADOS):

        # arquivo do cidade estados
        # se nao tem o extraido "desipado"
        if not path.exists(EXTRACT_FILE_CIDADES_ESTADOS):

            # se nao tem o arquivo baixado
            if not path.exists(ZIP_FILE_CIDADES_ESTADOS):

                # baixa o arquivo zip
                response = requests.get(URL_DOWNLOAD_CIDADES_ESTADOS)
                with open(ZIP_FILE_CIDADES_ESTADOS, "wb") as f:
                    f.write(response.content)

            # extrair o arquivo
            with zipfile.ZipFile(ZIP_FILE_CIDADES_ESTADOS, 'r') as zipRef:
                zipRef.extractall(EXTRACT_DIR)


        # arquivo das cordenadas
        # se nao tem o extraido "desipado"
        if not path.exists(EXTRACT_FILE_CORDENADAS):

            # se nao tem o arquivo baixado
            if not path.exists(ZIP_FILE_CORDENADAS):

                # baixa o arquivo zip
                response = requests.get(URL_DOWNLOAD_CORDENADAS)
                with open(ZIP_FILE_CORDENADAS, "wb") as f:
                    f.write(response.content)

            # extrair o arquivo
            with zipfile.ZipFile(ZIP_FILE_CORDENADAS, 'r') as zipRef:
                zipRef.extractall(EXTRACT_DIR)


        # processa o arquivo cidade estados
        df_cidades_estados = pd.read_excel(EXTRACT_FILE_CIDADES_ESTADOS, engine='odf', dtype=str, skiprows=6, usecols=[COLUNA_ESTADO, COLUNA_CIDADE, COLUNA_CODIGO_CIDADE])
        # nao tem duplicados entao nao faz diferença
        df_cidades_estados = df_cidades_estados.drop_duplicates()



        # processa o arquivo
        # Carrega o shapefile
        gdf = gpd.read_file(EXTRACT_FILE_CORDENADAS)

        # Reprojeta para um sistema métrico (UTM zone 23S - EPSG:31983)
        gdf_proj = gdf.to_crs(epsg=31983)

        # Calcula o centroide no sistema projetado e converte de volta para WGS84 (latitude/longitude)
        gdf[CENTROIDE] = gdf_proj.centroid.to_crs(epsg=4326)

        # Extrai latitude e longitude do centroide
        gdf[LATITUDE] = gdf[CENTROIDE].y
        gdf[LONGITUDE] = gdf[CENTROIDE].x

        # Seleciona colunas desejadas
        df_cordenadas = gdf[[CD_MUN, LATITUDE, LONGITUDE]]
        
        #renomeio no nome da coluna do codigo
        df_cordenadas = df_cordenadas.rename(columns={CD_MUN: COLUNA_CODIGO_CIDADE})

        # junta os dois arquivos de cordenada e de cidade estado
        df_completo = df_cordenadas.merge(df_cidades_estados, on= COLUNA_CODIGO_CIDADE, how= "left")
        
        # salva o arquivo
        df_completo.to_parquet(PARQUET_FILE_CIDADES_ESTADOS, index= False)

