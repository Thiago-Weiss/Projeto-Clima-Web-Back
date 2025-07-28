from os import cpu_count
from threading import Thread
from queue import Queue
import time
import shutil

# funcoes minhas 
from .verificarArquivos import verificar_arquivos
from .baixarArquivos import baixar_arquivos
from .descompactarArquivos import descompactar_arquivos
from .processarArquivos import processar_csvs
from app.services.obterDataBase.obterCidadesEstados import baixarArquivoCidadesEstados


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


    if False:
        shutil.rmtree(DOWNLOAD_DIR)
        shutil.rmtree(EXTRACT_DIR)


    print(f"Tempo total de execução: {time.time() - start:4f} segundos")



