import pandas as pd
from datetime import date

from app.services.graficos.utils import obter_lat_lon, obter_paths_por_cord_ano, gerar_data_frame, converter_para_o_front, validar_grafico_coluna_config
from app.core import PesquisaDiaMaisOpcoes, RespostaFormato
from app.core.const.clima import DATA
from app.core.const.respostasFront import GRAFICO, PERC_DADOS_VALIDOS, DADOS_TOTAIS
from app.core.const.pesquisaDiaMaisConfig import PESQUISA_DIA_MAIS_CONFIGS



def gerar_dados_pesquisa_dia_mais(
        estado: str, 
        cidade: str, 
        data_inicio: date, 
        data_fim: date,

        coluna_climatica: PesquisaDiaMaisOpcoes,

        dias_marge : int,
        resposta_formato : RespostaFormato,
    ):
    
    # valida a localizacao
    latitude, longitude = obter_lat_lon(cidade= cidade, estado= estado)
    if not latitude or not longitude:
        return f"Cordenadas nao encontrada para a cidade: {cidade} estado: {estado}"


    # data
    dt_inicio = pd.to_datetime(data_inicio)
    dt_fim = pd.to_datetime(data_fim)
    if dt_inicio > dt_fim:
        return f"Data de fim: {data_fim} maior que data de inicio: {data_inicio}"



    # pega a config padrao pra coluna
    coluna_config = PESQUISA_DIA_MAIS_CONFIGS.get(coluna_climatica)



    # verifica se tem dados historicos
    arquivo_paths = obter_paths_por_cord_ano(latitude, longitude, dt_inicio.year, dt_fim.year)
    if not arquivo_paths:
        return f"Sem dados historicos para {estado} {cidade}, no periodo de {data_inicio} a {data_fim}"


    # gera o dataframe 
    df, dados_totais, perc_validos = gerar_data_frame(arquivo_paths, coluna_config, dt_inicio, dt_fim)
    if df is None or df.empty:
        return f"Sem dados historicos para {estado} {cidade}, no periodo de {data_inicio} a {data_fim}"

    
    
    # filtra pelo dia mais 
    df[DATA] = pd.to_datetime(df[DATA])


    match coluna_climatica:
        case PesquisaDiaMaisOpcoes.MAIOR_TEMPERATURA:
            data_mais = df.loc[df[coluna_config[0].coluna.value].idxmax(), DATA]

        case PesquisaDiaMaisOpcoes.CHUVA:
            data_mais = df.loc[df[coluna_config[0].coluna.value].idxmax(), DATA]

        case PesquisaDiaMaisOpcoes.MENOR_TEMPERATURA:
            data_mais = df.loc[df[coluna_config[0].coluna.value].idxmin(), DATA]
            
            
    # pega uma margem de dias antes e depois
    dt_inicio = data_mais - pd.Timedelta(days= dias_marge)
    dt_fim = data_mais + pd.Timedelta(days= dias_marge)
    arquivo_paths = obter_paths_por_cord_ano(latitude, longitude, dt_inicio.year, dt_fim.year)
    
    # gera o novo data frame dos dias certos sem agrupar o dia
    df, _, _ = gerar_data_frame(arquivo_paths, coluna_config, dt_inicio, dt_fim, False)


    return {
        DADOS_TOTAIS: int(dados_totais),
        PERC_DADOS_VALIDOS: round(perc_validos, 2),
        GRAFICO: converter_para_o_front(df= df, formato= resposta_formato),
    }
