import pandas as pd


from app.core.const.clima import DATA, HORA
from app.core import EstacaoInfo, GraficoColunaConfig
from app.services.graficos.utils import abrir_data_frame, filtrar_por_datas, agrupar_dados_do_dia


# gera um dataframe do periodo inteiro de pesquisa e opcionalmente agrupa os dias para gerar menos pontos
def gerar_data_frame(
        arquivos : list[EstacaoInfo],
        grafico_coluna_config : list[GraficoColunaConfig], 
        dt_inicio : pd.Timestamp, 
        dt_fim : pd.Timestamp,
        agrupar_o_dia : bool = True) -> pd.DataFrame | None:
    

    dados_ausentes = 0
    dados_validos = 0
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


        # verifica quantos dados validos e ausentes eu tenho
        df_check = df.drop(columns=[DATA, HORA])
        dados_ausentes += df_check.isna().sum().sum()
        dados_validos  += df_check.notna().sum().sum()


        if agrupar_o_dia:
            df = agrupar_dados_do_dia(df, grafico_coluna_config)




        dfs_processados.append(df)
    
    if not dfs_processados:
        return None
    
    # crio um data frame unico com todos os dados
    df_grafico = pd.concat(dfs_processados, ignore_index=True)
    
    df_grafico[DATA] = pd.to_datetime(df_grafico[DATA])

    if agrupar_o_dia:
        # ordena só por dia 
        df_grafico = df_grafico.sort_values(DATA, ascending= True).reset_index(drop=True)
    else: 
        # ordena por dia e por hora
        df_grafico = df_grafico.sort_values([DATA, HORA], ascending=[True, True]).reset_index(drop=True)

    # estatisticas dos dados
    dados_totais = dados_validos + dados_ausentes
    perc_validos = 0
    if dados_totais > 0:
        perc_validos = (dados_validos / dados_totais) * 100


    return df_grafico, dados_totais, perc_validos