import requests
from concurrent.futures import ThreadPoolExecutor
from queue import Queue


# baixo todos os arquivos em "paralelo" ao mesmo tempo
def baixar_arquivos(arquivosParaBaixar : list, arquivosParaExtrair : Queue, maxThreads = 4):
    # baixa os arquivos zips
    def baixar_arquivo(anoUrlZip):
        ano, url, zipPath = anoUrlZip
        try:
            resposta = requests.get(url, stream=True)
            resposta.raise_for_status()
            # cria o arquivo e salva
            with open(zipPath, "wb") as f:
                for chunk in resposta.iter_content(chunk_size=8192):
                    f.write(chunk)

            print(f"✅ Download do ano {ano} concluído.")

            # coloca na fila de arquivos pra extrair
            arquivosParaExtrair.put((ano, zipPath))
        except Exception as e:
            print(f"❌ Erro ao baixar {url}: {e}")
    


    with ThreadPoolExecutor(max_workers=maxThreads) as executor:
        [executor.submit(baixar_arquivo, item) for item in arquivosParaBaixar]

    # terminou de baixar todos os arquivos e sinaliza para o processo de dizipar que nao tem mais nada
    arquivosParaExtrair.put(None)