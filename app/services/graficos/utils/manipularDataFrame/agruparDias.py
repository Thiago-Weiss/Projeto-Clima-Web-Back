import pandas as pd

from app.core.const.clima import DATA
from app.core import GraficoColunaConfig, FiltroGraficoAgrupamento






def agrupar_coluna(df: pd.DataFrame, coluna: str, modo: str, dias: int) -> pd.Series:
    match modo:
        case FiltroGraficoAgrupamento.SUM_DIA:
            return df[[coluna]].resample(f'{dias}D', origin= "start").sum()[coluna]
         
        case FiltroGraficoAgrupamento.MEAN_DIA:
            return df[[coluna]].resample(f'{dias}D', origin= "start").mean()[coluna]
         
        case FiltroGraficoAgrupamento.MAX_DIA:
            return df[[coluna]].resample(f'{dias}D', origin= "start").max()[coluna]
         
        case FiltroGraficoAgrupamento.MIN_DIA:
            return df[[coluna]].resample(f'{dias}D', origin= "start").min()[coluna]
         
        case _:
            return df[[coluna]].resample(f'{dias}D', origin= "start").max()[coluna]



def agrupar_dados_por_dias(df, agrupamento_dias,  grafico_coluna_config : list[GraficoColunaConfig]):

    # seta a data pra ser o index para manipulacao com o resaple
    df = df.set_index(DATA)

    # cria um novo data frame e adiciona a coluna data já com os dias agrupados
    df_agrupado = pd.DataFrame()
    #df_agrupado[DATA] = df.resample(f'{agrupamento_dias}D', origin= "start").mean().index
    #datas_agrupadas = df.resample(f'{agrupamento_dias}D', origin="start").groups.keys()
    df_agrupado[DATA] = df.resample(f'{agrupamento_dias}D', origin="start").asfreq().index

    # vai coluna por coluna agrupando os dados e prenchendo o novo dataframe 
    for var in grafico_coluna_config:
        coluna = var.coluna.value
        modo = var.modo_agrupamento
        df_agrupado[coluna] = agrupar_coluna(df, coluna, modo, agrupamento_dias).values
    
    return df_agrupado


