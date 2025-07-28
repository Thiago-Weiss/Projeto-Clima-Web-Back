import pandas as pd
from datetime import date

from app.services.graficos.utils import obter_lat_lon, obter_paths_por_cord_ano, gerar_data_frame, converter_df_para_objeto, validar_grafico_coluna_config
from app.core import ColunaClima, FiltroGraficoAgrupamento, DiaMais
from app.core.const.clima import DATA


def gerar_dados_grafico_dia_mais(
        estado: str, 
        cidade: str, 
        data_inicio: date, 
        data_fim: date,
        modo_dia: DiaMais, 
        colunas: list[ColunaClima],
        agrupamentos: list[FiltroGraficoAgrupamento],
        hora_fixa: list[int],
        janela_hora_inicio: list[int],
        janela_hora_fim: list[int],
        dias_marge : int):
    
    # valida a localizacao
    latitude, longitude = obter_lat_lon(cidade= cidade, estado= estado)
    if not latitude or not longitude:
        return f"Cordenadas nao encontrada para a cidade: {cidade} estado: {estado}"


    # data
    dt_inicio = pd.to_datetime(data_inicio)
    dt_fim = pd.to_datetime(data_fim)
    if dt_inicio > dt_fim:
        return f"Data de fim: {data_fim} maior que data de inicio: {data_inicio}"



    # valida a coluna e o modo de filtro
    coluna_configs = validar_grafico_coluna_config(colunas, agrupamentos, hora_fixa, janela_hora_inicio, janela_hora_fim)
    if isinstance(coluna_configs, str):
        return coluna_configs

    # verifica se tem dados historicos
    arquivo_paths = obter_paths_por_cord_ano(latitude, longitude, dt_inicio.year, dt_fim.year)
    if not arquivo_paths:
        return f"Sem dados historicos para {estado} {cidade}, no periodo de {data_inicio} a {data_fim}"



    # gera o dataframe 
    df = gerar_data_frame(arquivo_paths, coluna_configs, dt_inicio, dt_fim)
    if df is None or df.empty:
        return f"Sem dados historicos para {estado} {cidade}, no periodo de {data_inicio} a {data_fim}"

    
    
    # filtra pelo dia mais 
    df[DATA] = pd.to_datetime(df[DATA])
    if modo_dia == DiaMais.DIA_MAX:
        data_mais = df.loc[df[coluna_configs[0].coluna.value].idxmax(), DATA]
    else:
        data_mais = df.loc[df[coluna_configs[0].coluna.value].idxmin(), DATA]

    # pega uma margem de dias antes e depois
    dt_inicio = data_mais - pd.Timedelta(days= dias_marge)
    dt_fim = data_mais + pd.Timedelta(days= dias_marge)
    arquivo_paths = obter_paths_por_cord_ano(latitude, longitude, dt_inicio.year, dt_fim.year)
    
    # gera o novo data frame dos dias certos sem agrupar o dia
    df = gerar_data_frame(arquivo_paths, coluna_configs, dt_inicio, dt_fim, False)

    return converter_df_para_objeto(df)

