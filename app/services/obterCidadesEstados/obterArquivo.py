import os
import requests
import zipfile
import pandas as pd
import shutil

# meus arquivos
from app.core.arquivosPaths.estadosCidades import *



def baixarArquivoCidadesEstados():

    # garante que as pastas existem
    os.makedirs(ZIP_DIR, exist_ok=True)
    os.makedirs(EXTRACT_DIR, exist_ok=True)
    os.makedirs(PARQUET_DIR, exist_ok=True)


    # se nao tem o arquivo final
    if not os.path.exists(PARQUET_FILE):

        # se nao tem o extraido "desipado"
        if not os.path.exists(EXTRACT_FILE):

            # se nao tem o arquivo baixado
            if not os.path.exists(ZIP_FILE):

                response = requests.get(URL_DOWNLOAD)
                with open(ZIP_FILE, "wb") as f:
                    f.write(response.content)

            # extrair o arquivo
            with zipfile.ZipFile(ZIP_FILE, 'r') as zipRef:
                zipRef.extractall(EXTRACT_DIR)

        # processa o arquivo
        df = pd.read_excel(EXTRACT_FILE, engine='odf', dtype=str, skiprows=6, usecols=[COLUNA_ESTADO, COLUNA_CIDADE])
        df = df.groupby(COLUNA_ESTADO)[COLUNA_CIDADE].apply(list).reset_index()
        df.to_parquet(PARQUET_FILE, index=False)


    # remove os arquivos temporarios
    shutil.rmtree(ZIP_DIR)
    shutil.rmtree(EXTRACT_DIR)



