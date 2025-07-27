import pandas as pd
from datetime import date


from app.core.utils import obter_lat_lon, obter_paths_por_cord_ano
from app.core.const.clima import COLUNAS_PADRAO, DATA
from app.core.utils.gerarDataFrame.gerar import gerar_data_frame
from app.core.utils.gerarDataFrame.gerarDia import gerar_data_frame_dia

from app.core.dataclass import GraficoColunaConfig
from app.core.enums import ColunaClima, FiltroGraficoAgrupamento




def gerar_dados_dia_grafico(estado: str, cidade: str, data_inicio: date, data_fim: date, coluna: str) -> dict:
    
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

    # coluna de testes 
    config = GraficoColunaConfig(
        coluna=ColunaClima.PRECIPITACAO,     
        filtro=FiltroGraficoAgrupamento.SUM_DIA,        
        hora_fixa=23,                        
        janela_horas=(10, 12)                
    )
    coluna_teste = [config]

    
    # gera o dataframe de todo o periodo com os dados 
    df = gerar_data_frame(arquivo_paths, coluna_teste, dt_inicio, dt_fim)
    if df is None or df.empty:
        return f"Sem dados historicos para {estado} {cidade}, no periodo de {data_inicio} a {data_fim}"
    

    df[DATA] = pd.to_datetime(df[DATA]) 
    data_max = df.loc[df[config.coluna.value].idxmax(), DATA]

    dt_inicio = data_max - pd.Timedelta(days=1)
    dt_fim = data_max + pd.Timedelta(days=1)
    arquivo_paths = obter_paths_por_cord_ano(latitude, longitude, dt_inicio.year, dt_fim.year)
    
    df = gerar_data_frame_dia(arquivo_paths, coluna_teste, dt_inicio, dt_fim)

    df_copy = df.copy()
    df_copy[DATA] = df_copy[DATA].dt.strftime('%Y-%m-%d')


    return df_copy.values.tolist()
