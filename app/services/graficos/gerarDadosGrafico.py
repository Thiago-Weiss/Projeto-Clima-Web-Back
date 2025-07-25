# app/services/grafico.py

import pandas as pd
from datetime import datetime

from app.core.utils import obter_lat_lon, obter_paths_por_cord_ano
from app.core.arquivosPaths.clima import COLUNAS_PADRAO
from app.core.utils.gerarDataFrame.gerar import gerar_data_frame


from app.core.dataclass import GraficoColunaConfig
from app.core.enums import ColunaClima, FiltroGrafico
from app.core.arquivosPaths.clima import DATA



def gerar_dados_grafico(estado: str, cidade: str, data_inicio: str, data_fim: str, coluna: str) -> dict:
    
    # validad a localizacao
    latitude, longitude = obter_lat_lon(cidade= cidade, estado= estado)
    if not latitude or not longitude:
        raise ValueError(f"Coordenadas não encontradas para: {cidade}, {estado}. Verifique os dados.")


    # valida a data
    try:
        dt_inicio = pd.to_datetime(data_inicio)
        dt_fim = pd.to_datetime(data_fim)
    except Exception:
        raise ValueError("Formato de data inválido. Use YYYY-MM-DD.")

    if dt_inicio > dt_fim:
        raise ValueError("Data de início não pode ser depois da data de dt_fim.")


    # verifica se a coluna existe nas tabelas de clima
    if not coluna in COLUNAS_PADRAO:
        raise ValueError(f"Não existe a coluna {coluna} nas tabelas")




    # verifica se tem dados historicos
    arquivo_paths = obter_paths_por_cord_ano(latitude, longitude, dt_inicio.year, dt_fim.year)
    if not arquivo_paths:
        raise ValueError(f"Sem dados historicos para {estado} {cidade}, no periodo de {data_inicio} a {data_fim}")

    config = GraficoColunaConfig(
        coluna=ColunaClima.PRECIPITACAO,     
        filtro=FiltroGrafico.SUM_DIA,        
        hora_fixa=23,                        
        janela_horas=(10, 12)                
    )
    coluna_teste = [config]

    
    df = gerar_data_frame(arquivo_paths, coluna_teste, dt_inicio, dt_fim)
    if df is None or df.empty:
        raise ValueError("Erro interno ao gerar o data frame do grafico")
    
    df_copy = df.copy()
    df_copy[DATA] = df_copy[DATA].dt.strftime('%Y-%m-%d')

    return df_copy.values.tolist()
