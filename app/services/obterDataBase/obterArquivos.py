from os import cpu_count
from threading import Thread
from queue import Queue
import time
import shutil

# funcoes minhas 
from .obterClima.verificarArquivos import verificar_arquivos
from .obterClima.baixarArquivos import baixar_arquivos
from .obterClima.descompactarArquivos import descompactar_arquivos
from .obterClima.processarArquivos import processar_csvs
from app.services.obterDataBase.obterCidadesEstados import baixarArquivoCidadesEstados

from app.core.const.basePath import DOWNLOAD_DIR_BASE, EXTRACT_DIR_BASE
from app.core.const.estadosCidades import ZIP_DIR, EXTRACT_DIR


# verifica/ cria todo o data base
def iniciar_arquivos():
    start = time.time()
    
    # Filas para comunicação entre estágios
    arquivosParaBaixar = []
    arquivosParaExtrair = Queue()
    arquivosParaTratar = Queue()

    verificar_arquivos(arquivosParaBaixar, arquivosParaExtrair, arquivosParaTratar)
    t1 = Thread(target= baixar_arquivos, args=(arquivosParaBaixar, arquivosParaExtrair, 2,), daemon= True)
    t2 = Thread(target= descompactar_arquivos, args=(arquivosParaExtrair, arquivosParaTratar, 2,), daemon= True)
    t3 = Thread(target= processar_csvs, args=(arquivosParaTratar, max(1, cpu_count() - 5),), daemon= True)
    t4 = Thread(target= baixarArquivoCidadesEstados, daemon= True)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()


    # remove os arquivos base
    if False:
        shutil.rmtree(DOWNLOAD_DIR_BASE)
        shutil.rmtree(EXTRACT_DIR_BASE)


    print(f"Tempo total de execução: {time.time() - start:4f} segundos")



