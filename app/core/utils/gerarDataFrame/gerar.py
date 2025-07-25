
from os import path
import pandas as pd


from app.core.dataclass import EstacaoInfo, GraficoColunaConfig
from app.core.arquivosPaths.clima import HORA, DATA
from app.core.enums import FiltroGrafico


def gerar_data_frame(
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
        df = df[(df[DATA] >= dt_inicio) & (df[DATA] <= dt_fim)]
        df = df.sort_values(DATA).reset_index(drop=True)

        # cria um df_resultado só com os DIAS do ano em ordem cronologica, sem as outras colunas
        df_resultado = pd.DataFrame({DATA : df[DATA].unique()})



        # preenche o resto das colunas do df_resultado usando as config das colunas 
        for config in grafico_coluna_config:
            #configs
            coluna = config.coluna.value
            filtro = config.filtro
            hora_fixa = config.hora_fixa
            janela_horas = config.janela_horas

            # copia do data frame principal com a coluna que vai ser filtrada
            df_temp = df[[DATA, HORA, coluna]].copy()

            match filtro:
                case FiltroGrafico.MAX_DIA:
                    agg = df_temp.groupby(DATA)[coluna].max().rename(coluna)

                case FiltroGrafico.MIN_DIA:
                    agg = df_temp.groupby(DATA)[coluna].min().rename(coluna)

                case FiltroGrafico.MEAN_DIA:
                    agg = df_temp.groupby(DATA)[coluna].mean().rename(coluna)

                case FiltroGrafico.SUM_DIA:
                    agg = df_temp.groupby(DATA)[coluna].sum().rename(coluna)

                case FiltroGrafico.HORA_FIXA:
                    df_temp = df_temp[df_temp[HORA] == hora_fixa]
                    agg = df_temp.set_index(DATA)[coluna]

                case FiltroGrafico.HORA_MIN_JANELA:
                    ini, fim = janela_horas
                    df_temp = df_temp[(df_temp[HORA] >= ini) & (df_temp[HORA] <= fim)]
                    agg = df_temp.groupby(DATA)[coluna].min().rename(coluna)

                case FiltroGrafico.HORA_MAX_JANELA:
                    ini, fim = janela_horas
                    df_temp = df_temp[(df_temp[HORA] >= ini) & (df_temp[HORA] <= fim)]
                    agg = df_temp.groupby(DATA)[coluna].max().rename(coluna)

                case FiltroGrafico.HORA_MEAN_JANELA:
                    ini, fim = janela_horas
                    df_temp = df_temp[(df_temp[HORA] >= ini) & (df_temp[HORA] <= fim)]
                    agg = df_temp.groupby(DATA)[coluna].mean().rename(coluna)


                case _:
                    raise ValueError(f"Modo de filtro inválido: {filtro}")

            df_resultado = df_resultado.merge(agg.reset_index(), on=DATA, how="left")
        dfs_processados.append(df_resultado)
    
    if not dfs_processados:
        return None
    
    df_grafico = pd.concat(dfs_processados, ignore_index=True)
    df_grafico[DATA] = pd.to_datetime(df_grafico[DATA])
    df_grafico = df_grafico.sort_values(DATA).reset_index(drop=True)

    return df_grafico