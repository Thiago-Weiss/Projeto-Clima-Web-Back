import pandas as pd
from app.core.const.clima import DATA, HORA
from app.core import FiltroGraficoAgrupamento, GraficoColunaConfig


def agrupar_dados_por_dia(df : pd.DataFrame, grafico_coluna_config : list[GraficoColunaConfig]):
    # cria um df_resultado só com os DIAS do ano em ordem cronologica, sem as outras colunas
    df_resultado = pd.DataFrame({DATA : df[DATA].unique()})

    # preenche o resto das colunas do df_resultado usando as config das colunas 
    for config in grafico_coluna_config:
        #configs
        coluna = config.coluna.value
        filtro = config.modo_agrupamento
        hora_fixa = config.hora_fixa
        janela_horas = (config.hora_janela_inicio, config.hora_janela_fim)

        # copia do data frame principal com a coluna que vai ser filtrada
        df_temp = df[[DATA, HORA, coluna]].copy()

        match filtro:
            case FiltroGraficoAgrupamento.MAX_DIA:
                agg = df_temp.groupby(DATA)[coluna].max().rename(coluna)

            case FiltroGraficoAgrupamento.MIN_DIA:
                agg = df_temp.groupby(DATA)[coluna].min().rename(coluna)

            case FiltroGraficoAgrupamento.MEAN_DIA:
                agg = df_temp.groupby(DATA)[coluna].mean().rename(coluna)

            case FiltroGraficoAgrupamento.SUM_DIA:
                agg = df_temp.groupby(DATA)[coluna].sum().rename(coluna)

            case FiltroGraficoAgrupamento.HORA_FIXA:
                df_temp = df_temp[df_temp[HORA] == hora_fixa]
                agg = df_temp.set_index(DATA)[coluna]

            case FiltroGraficoAgrupamento.HORA_MIN_JANELA:
                ini, fim = janela_horas
                df_temp = df_temp[(df_temp[HORA] >= ini) & (df_temp[HORA] <= fim)]
                agg = df_temp.groupby(DATA)[coluna].min().rename(coluna)

            case FiltroGraficoAgrupamento.HORA_MAX_JANELA:
                ini, fim = janela_horas
                df_temp = df_temp[(df_temp[HORA] >= ini) & (df_temp[HORA] <= fim)]
                agg = df_temp.groupby(DATA)[coluna].max().rename(coluna)

            case FiltroGraficoAgrupamento.HORA_MEAN_JANELA:
                ini, fim = janela_horas
                df_temp = df_temp[(df_temp[HORA] >= ini) & (df_temp[HORA] <= fim)]
                agg = df_temp.groupby(DATA)[coluna].mean().rename(coluna)


            case _:
                raise ValueError(f"Modo de filtro inválido: {filtro}")

        df_resultado = df_resultado.merge(agg.reset_index(), on=DATA, how="left")

    return df_resultado