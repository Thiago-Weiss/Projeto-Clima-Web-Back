import pandas as pd
from datetime import date

from app.services.graficos.utils import obter_lat_lon, obter_paths_por_cord_ano, gerar_data_frame, converter_para_o_front, validar_grafico_coluna_config, agrupar_dados_por_dias, pegar_dados_das_estacoes_pesquisadas
from app.core import ColunaClima, FiltroGraficoAgrupamento, RespostaFormato
from app.core.const.respostasFront import GRAFICO, PERC_DADOS_VALIDOS, DADOS_TOTAIS, ESTACOES_DADOS



def gerar_dados_pesquisa_avancada(
        estado: str, 
        cidade: str, 
        data_inicio: date, 
        data_fim: date, 

        colunas: list[ColunaClima],
        agrupamentos: list[FiltroGraficoAgrupamento],
        hora_fixa: list[int],
        janela_hora_inicio: list[int],
        janela_hora_fim: list[int],

        dados_agrupados_por_x_dias: int,
        resposta_formato : RespostaFormato,
    ):
    
    # valida a localizacao
    latitude, longitude = obter_lat_lon(cidade= cidade, estado= estado)
    if not latitude or not longitude:
        return f"Cordenadas nao encontrada para a cidade: {cidade} estado: {estado}"


    # valida data
    dt_inicio = pd.to_datetime(data_inicio)
    dt_fim = pd.to_datetime(data_fim)
    if dt_inicio > dt_fim:
        return f"Data de fim: {data_fim} maior que data de inicio: {data_inicio}"


    # valida a coluna e o modo de filtro
    coluna_configs = validar_grafico_coluna_config(colunas, agrupamentos, hora_fixa, janela_hora_inicio, janela_hora_fim, False)
    if isinstance(coluna_configs[0], str):
        return coluna_configs



    # verifica se tem dados historicos
    arquivo_paths = obter_paths_por_cord_ano(latitude, longitude, dt_inicio.year, dt_fim.year)
    if not arquivo_paths:
        return f"Sem dados historicos para {estado} {cidade}, no periodo de {data_inicio} a {data_fim}"

    # gera o dataframe 
    df, dados_totais, perc_validos = gerar_data_frame(arquivo_paths, coluna_configs, dt_inicio, dt_fim)
    if df is None or df.empty:
        return f"Sem dados historicos para {estado} {cidade}, no periodo de {data_inicio} a {data_fim}"


    # agrupa dias de dados gerando menos pontos no grafico
    if dados_agrupados_por_x_dias:
        df = agrupar_dados_por_dias(df, dados_agrupados_por_x_dias, coluna_configs)


    return {
        DADOS_TOTAIS: int(dados_totais),
        PERC_DADOS_VALIDOS: round(perc_validos, 2),
        ESTACOES_DADOS: pegar_dados_das_estacoes_pesquisadas(arquivo_paths),
        GRAFICO: converter_para_o_front(df= df, formato= resposta_formato),
    }
 

