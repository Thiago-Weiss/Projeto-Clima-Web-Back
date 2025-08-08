import pandas as pd
from datetime import date

from app.services.graficos.utils import obter_lat_lon, obter_paths_por_cord_ano, gerar_data_frame, converter_para_o_front, agrupar_dados_por_dias, pegar_dados_das_estacoes_pesquisadas
from app.core import RespostaFormato, PesquisaSimplesOpcoes
from app.core.const.respostasFront import GRAFICO, PERC_DADOS_VALIDOS, DADOS_TOTAIS, ESTACOES_DADOS
from app.core.const.pesquisaSimplesConfig import PESQUISA_SIMPLES_CONFIGS


def gerar_dados_pesquisa_simples(
        estado: str, 
        cidade: str, 
        data_inicio: date, 
        data_fim: date, 

        coluna_climatica: PesquisaSimplesOpcoes,
        
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


    # pega a config padrao pra coluna
    coluna_config = PESQUISA_SIMPLES_CONFIGS.get(coluna_climatica)


    # verifica se tem dados historicos
    arquivo_paths = obter_paths_por_cord_ano(latitude, longitude, dt_inicio.year, dt_fim.year)
    if not arquivo_paths:
        return f"Sem dados historicos para {estado} {cidade}, no periodo de {data_inicio} a {data_fim}"

    # gera o dataframe 
    df, dados_totais, perc_validos = gerar_data_frame(arquivo_paths, coluna_config, dt_inicio, dt_fim)
    if df is None or df.empty:
        return f"Sem dados historicos para {estado} {cidade}, no periodo de {data_inicio} a {data_fim}"


    # agrupa dias de dados gerando menos pontos no grafico
    if dados_agrupados_por_x_dias:
        df = agrupar_dados_por_dias(df, dados_agrupados_por_x_dias, coluna_config)


    return {
        DADOS_TOTAIS: int(dados_totais),
        PERC_DADOS_VALIDOS: round(perc_validos, 2),
        ESTACOES_DADOS: pegar_dados_das_estacoes_pesquisadas(arquivo_paths),
        GRAFICO: converter_para_o_front(df= df, formato= resposta_formato),
    }
 

