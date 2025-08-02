from os import path
import pandas as pd

from app.core.const.index import INDEX_DIR, LATITUDE, LONGITUDE, ARQUIVO, ESTACAO, DISTANCIA
from app.services.graficos.utils import calcular_distancia_direcao, abrir_data_frame
from app.core import EstacaoInfo
from app.core.const.basePath import BASE_DIR

def obter_paths_por_cord_ano(
        latitude : float,
        longitude : float, 
        ano_inicio : int, 
        ano_fim : int, 
        distancia_max : float = 50) -> list[EstacaoInfo] | None:

    resultados = []
    for ano in range(ano_inicio, ano_fim + 1):
        # dados do arquivo
        arquivo = path.join(INDEX_DIR, f"index{ano}.parquet")
        colunas = [LATITUDE, LONGITUDE, ARQUIVO, ESTACAO]
        
        # abre o arquivo
        df =  abrir_data_frame(arquivo, colunas)
        if df is None:
            continue


        # Calcula a distância para todas as estações
        df[[DISTANCIA]] = df.apply(
            lambda row: pd.Series(calcular_distancia_direcao(latitude, longitude, row[LATITUDE], row[LONGITUDE])[0]),
            axis=1
        )
        # Filtra estações dentro da distância máxima
        df_filtrado = df[df[DISTANCIA] <= distancia_max]


        # vai para o proximo ano se nao tiver achado a estacao
        if df_filtrado.empty:
            continue

        # Encontra a estação mais próxima
        estacao = df_filtrado.nsmallest(1, DISTANCIA).iloc[0]


        # path do pc que está rodando mais parte local
        arquivo_path = BASE_DIR / estacao[ARQUIVO]
        print(arquivo_path)
        # adiciona a lista os dados da estacao
        resultados.append(
            EstacaoInfo(
                arquivo= arquivo_path,
                latitude= estacao[LATITUDE],
                longitude= estacao[LONGITUDE],
                estacao= estacao[ESTACAO]
                ))
        
    if resultados:
        return resultados
    return None