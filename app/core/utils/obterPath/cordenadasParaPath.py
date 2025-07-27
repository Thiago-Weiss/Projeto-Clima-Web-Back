from os import path
import pandas as pd

from app.core.const.index import INDEX_DIR, LATITUDE, LONGITUDE, ARQUIVO, ESTACAO, DISTANCIA
from app.core.utils.calcularDistanciaDirecao.calcular import calcular_distancia_direcao
from app.core.dataclass import EstacaoInfo

def obter_paths_por_cord_ano(latitude : float, longitude : float, ano_inicio : int, ano_fim : int, distancia_max : float = 50) -> list[EstacaoInfo] | None:

    resultados = []
    for ano in range(ano_inicio, ano_fim + 1):
        indexPath = path.join(INDEX_DIR, f"index{ano}.parquet")
        
        # verifica se o path existe
        if not path.exists(indexPath):
            continue


        # abre o arquivo
        colunas = [LATITUDE, LONGITUDE, ARQUIVO, ESTACAO]
        df = pd.read_parquet(indexPath, columns= colunas)


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

        # adiciona a lista os dados da estacao
        resultados.append(
            EstacaoInfo(
                arquivo= estacao[ARQUIVO],
                latitude= estacao[LATITUDE],
                longitude= estacao[LONGITUDE],
                estacao= estacao[ESTACAO]
                ))
        
    if resultados:
        return resultados
    return None