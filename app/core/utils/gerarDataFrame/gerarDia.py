
from os import path
import pandas as pd


from app.core.dataclass import EstacaoInfo, GraficoColunaConfig
from app.core.const.clima import HORA, DATA
from app.core.enums import FiltroGraficoAgrupamento


def gerar_data_frame_dia(
        arquivos : list[EstacaoInfo],
        grafico_coluna_config : list[GraficoColunaConfig], 
        dt_inicio : pd.Timestamp, 
        dt_fim : pd.Timestamp) -> pd.DataFrame | None:
    
    dfs_processados = []
    for estacao in arquivos:
        # verifica se o arquivo existe
        arquivo = estacao.arquivo
        if not path.exists(arquivo):
            continue

        # pega os nomes das culunas que vai ser importado
        colunas = list(var.coluna.value for var in grafico_coluna_config)

        # abre o arquivo
        df = pd.read_parquet(arquivo, columns= [DATA, HORA] + colunas)

        # filtra pelo periodo de tempo
        df[DATA] = pd.to_datetime(df[DATA])        
        df = df[(df[DATA] >= dt_inicio) & (df[DATA] <= dt_fim)].reset_index(drop= True)

        dfs_processados.append(df)
    
    if not dfs_processados:
        return None
    
    df_grafico = pd.concat(dfs_processados, ignore_index=True)


    return df_grafico