import os
import zipfile
from concurrent.futures import ThreadPoolExecutor
import shutil
from queue import Queue

from app.core.arquivosPaths.clima import EXTRACT_DIR



# comeca a desipar os arquivos já baixados em "paralelo" ao mesmo tempo
def descompactar_arquivos(arquivosParaExtrair : Queue, arquivosParaTratar : Queue,  maxThreads=4):
    # deszipa os arquivo
    def descompactar_arquivo(arquivo):
        ano, zipPath = arquivo
        dir = os.path.join(EXTRACT_DIR, str(ano))
        os.makedirs(dir, exist_ok=True)

        # desizpa o arquivo e salva tudo em uma pasta de nome {ano} dentro da pasta de extraidos
        with zipfile.ZipFile(zipPath, 'r') as zip_ref:
            for member in zip_ref.infolist():

                filename = os.path.basename(member.filename)
                if not filename:
                    # iginora as pastas
                    continue
                source = zip_ref.open(member)
                target_path = os.path.join(dir, filename)
                with open(target_path, "wb") as target:
                    shutil.copyfileobj(source, target)


        print(f"[📦] Descompactado: {zipPath}")

        # coloca na fila de arquivos pra processar
        arquivosParaTratar.put((ano, dir))

    with ThreadPoolExecutor (max_workers =maxThreads) as executor:
        while True:
            arquivo = arquivosParaExtrair.get()
            if arquivo is None:
                break

            executor.submit(descompactar_arquivo, arquivo)
    arquivosParaTratar.put(None)
