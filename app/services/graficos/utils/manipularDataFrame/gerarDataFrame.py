import pandas as pd


from app.core.const.clima import DATA, HORA
from app.core import EstacaoInfo, GraficoColunaConfig
from app.services.graficos.utils import abrir_data_frame, filtrar_por_datas, agrupar_dados_por_dia



def gerar_data_frame(
        arquivos : list[EstacaoInfo],
        grafico_coluna_config : list[GraficoColunaConfig], 
        dt_inicio : pd.Timestamp, 
        dt_fim : pd.Timestamp,
        agrupar_dias : bool = True) -> pd.DataFrame | None:
    
    dfs_processados = []
    for estacao in arquivos:
        # dados do arquivo
        arquivo = estacao.arquivo
        colunas = list(var.coluna.value for var in grafico_coluna_config) + [DATA, HORA]

        # abre o arquivo
        df = abrir_data_frame(arquivo, colunas)
        if df is None:
            return

        # filtra pelo periodo de tempo
        df = filtrar_por_datas(df, dt_inicio, dt_fim)
        if agrupar_dias:
            df = agrupar_dados_por_dia(df, grafico_coluna_config)

        dfs_processados.append(df)
    
    if not dfs_processados:
        return None
    
    df_grafico = pd.concat(dfs_processados, ignore_index=True)
    
    return df_grafico