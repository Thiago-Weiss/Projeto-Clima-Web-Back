import pandas as pd
from datetime import date

from app.services.graficos.utils import obter_lat_lon, obter_paths_por_cord_ano, gerar_data_frame, converter_df_para_list
from app.core import GraficoColunaConfig, ColunaClima, FiltroGraficoAgrupamento
from app.core.const.clima import COLUNAS_PADRAO, DATA



def gerar_dados_grafico_dia_mais(estado: str, cidade: str, data_inicio: date, data_fim: date, coluna: str, dias_marge : int = 1) -> dict:
    
    # valida a localizacao
    latitude, longitude = obter_lat_lon(cidade= cidade, estado= estado)
    if not latitude or not longitude:
        return f"Cordenadas nao encontrada para a cidade: {cidade} estado: {estado}"


    # data
    dt_inicio = pd.to_datetime(data_inicio)
    dt_fim = pd.to_datetime(data_fim)
    if dt_inicio > dt_fim:
        return f"Data de fim: {data_fim} maior que data de inicio: {data_inicio}"


    # verifica se a coluna existe nas tabelas de clima
    if not coluna in COLUNAS_PADRAO:
        raise ValueError(f"Não existe a coluna {coluna} nas tabelas")




    # verifica se tem dados historicos
    arquivo_paths = obter_paths_por_cord_ano(latitude, longitude, dt_inicio.year, dt_fim.year)
    if not arquivo_paths:
        return f"Sem dados historicos para {estado} {cidade}, no periodo de {data_inicio} a {data_fim}"

    config = GraficoColunaConfig(
        coluna=ColunaClima.PRECIPITACAO,     
        filtro=FiltroGraficoAgrupamento.SUM_DIA,        
        hora_fixa=23,                        
        janela_horas=(10, 12)                
    )
    coluna_teste = [config]


    # gera o dataframe 
    df = gerar_data_frame(arquivo_paths, coluna_teste, dt_inicio, dt_fim)
    if df is None or df.empty:
        return f"Sem dados historicos para {estado} {cidade}, no periodo de {data_inicio} a {data_fim}"

    

    # filtra pelo dia mais 
    df[DATA] = pd.to_datetime(df[DATA]) 
    data_max = df.loc[df[config.coluna.value].idxmax(), DATA]

    # pega uma margem de dias antes e depois
    dt_inicio = data_max - pd.Timedelta(days= dias_marge)
    dt_fim = data_max + pd.Timedelta(days= dias_marge)
    arquivo_paths = obter_paths_por_cord_ano(latitude, longitude, dt_inicio.year, dt_fim.year)
    
    # gera o novo data frame dos dias certos sem agrupar o dia
    df = gerar_data_frame(arquivo_paths, coluna_teste, dt_inicio, dt_fim, False)

    return converter_df_para_list(df)

