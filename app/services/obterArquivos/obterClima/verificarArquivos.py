import os
from queue import Queue

# meus arquivos
from app.core.arquivosPaths.clima import ZIP_DIR, EXTRACT_DIR, PARQUET_DIR, ANO_INICIO, ANO_FINAL, URL_DOWNLOAD
from app.core.arquivosPaths.index import INDEX_DIR






os.makedirs(ZIP_DIR, exist_ok=True)
os.makedirs(EXTRACT_DIR, exist_ok=True)
os.makedirs(PARQUET_DIR, exist_ok=True)



def verificar_arquivos(arquivosParaBaixar : list, arquivosParaExtrair : Queue, arquivosParaTratar : Queue):
    def contar_arquivos(diretorio):
        if os.path.exists(diretorio) and os.path.isdir(diretorio):
            return len([f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))])
        return 0

    for ano in range(ANO_INICIO, ANO_FINAL + 1):
        zipAnoFile = os.path.join(ZIP_DIR, f"{ano}.zip")
        extraidosAnoDir = os.path.join(EXTRACT_DIR, str(ano))
        indexAnoFile = os.path.join(INDEX_DIR, f"index{ano}.parquet")
        parquetAnoDir = os.path.join(PARQUET_DIR, str(ano))

        # se nao tiver os arquivos na pasta parquet
        if not os.path.exists(indexAnoFile) or contar_arquivos(parquetAnoDir) < 4:
        # verifica os arquivos na pasta de arquivos extraidos
        
            # tem os arquivos extraidos e falta tratar
            if contar_arquivos(extraidosAnoDir) > 4:
                # coloca na fila para tratar os arquivos
                arquivosParaTratar.put((ano, extraidosAnoDir))

            # nao tem os arquivos extraidos
            elif contar_arquivos(extraidosAnoDir) < 4:
            # verifica se tem o arquivo zip baixado
                # tem o arquivo zip baixado 
                if os.path.exists(zipAnoFile):
                    # coloca na fila para extrair
                    arquivosParaExtrair.put((ano, zipAnoFile))

                # nao tem o arquivo zip baixado
                else:
                    # coloca na lista para baixar
                    url = f"{URL_DOWNLOAD}{ano}.zip"
                    arquivosParaBaixar.append((ano, url, zipAnoFile))
