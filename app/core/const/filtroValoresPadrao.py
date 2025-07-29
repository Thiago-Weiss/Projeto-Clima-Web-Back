from app.core import ColunaClima, FiltroGraficoAgrupamento




MODO_AGRUPAMENTO = {
    ColunaClima.PRECIPITACAO : FiltroGraficoAgrupamento.SUM_DIA,
    ColunaClima.PRESSAO : FiltroGraficoAgrupamento.MEAN_DIA,
    ColunaClima.PRESSAO_MAX : FiltroGraficoAgrupamento.MAX_DIA,
    ColunaClima.PRESSAO_MIN : FiltroGraficoAgrupamento.MIN_DIA,
    ColunaClima.RADIACAO : FiltroGraficoAgrupamento.MEAN_DIA,
    ColunaClima.TEMP_AR : FiltroGraficoAgrupamento.MAX_DIA,
    ColunaClima.TEMP_ORVALHO : FiltroGraficoAgrupamento.MAX_DIA,
    ColunaClima.TEMP_MAX : FiltroGraficoAgrupamento.MAX_DIA,
    ColunaClima.TEMP_MIN : FiltroGraficoAgrupamento.MAX_DIA,
    ColunaClima.ORVALHO_MAX : FiltroGraficoAgrupamento.MAX_DIA,
    ColunaClima.ORVALHO_MIN : FiltroGraficoAgrupamento.MAX_DIA,
    ColunaClima.UMIDADE_MAX : FiltroGraficoAgrupamento.MAX_DIA,
    ColunaClima.UMIDADE_MIN : FiltroGraficoAgrupamento.MAX_DIA,
    ColunaClima.UMIDADE : FiltroGraficoAgrupamento.MAX_DIA,
    ColunaClima.VENTO_DIRECAO : FiltroGraficoAgrupamento.MAX_DIA,
    ColunaClima.VENTO_RAJADA : FiltroGraficoAgrupamento.MAX_DIA,
    ColunaClima.VENTO_VELOCIDADE : FiltroGraficoAgrupamento.MAX_DIA,
}


HORA_FIXA = {
    ColunaClima.PRECIPITACAO : 10,
    ColunaClima.PRESSAO : 10,
    ColunaClima.PRESSAO_MAX : 10,
    ColunaClima.PRESSAO_MIN : 10,
    ColunaClima.RADIACAO : 10,
    ColunaClima.TEMP_AR : 10,
    ColunaClima.TEMP_ORVALHO : 10,
    ColunaClima.TEMP_MAX : 10,
    ColunaClima.TEMP_MIN : 10,
    ColunaClima.ORVALHO_MAX : 10,
    ColunaClima.ORVALHO_MIN : 10,
    ColunaClima.UMIDADE_MAX : 10,
    ColunaClima.UMIDADE_MIN : 10,
    ColunaClima.UMIDADE : 10,
    ColunaClima.VENTO_DIRECAO : 10,
    ColunaClima.VENTO_RAJADA : 10,
    ColunaClima.VENTO_VELOCIDADE : 10,
}

HORA_JANELA_INICIO = {
    ColunaClima.PRECIPITACAO : 10,
    ColunaClima.PRESSAO : 10,
    ColunaClima.PRESSAO_MAX : 10,
    ColunaClima.PRESSAO_MIN : 10,
    ColunaClima.RADIACAO : 10,
    ColunaClima.TEMP_AR : 10,
    ColunaClima.TEMP_ORVALHO : 10,
    ColunaClima.TEMP_MAX : 10,
    ColunaClima.TEMP_MIN : 10,
    ColunaClima.ORVALHO_MAX : 10,
    ColunaClima.ORVALHO_MIN : 10,
    ColunaClima.UMIDADE_MAX : 10,
    ColunaClima.UMIDADE_MIN : 10,
    ColunaClima.UMIDADE : 10,
    ColunaClima.VENTO_DIRECAO : 10,
    ColunaClima.VENTO_RAJADA : 10,
    ColunaClima.VENTO_VELOCIDADE : 10,
}

HORA_JANELA_FIM = {
    ColunaClima.PRECIPITACAO : 10,
    ColunaClima.PRESSAO : 10,
    ColunaClima.PRESSAO_MAX : 10,
    ColunaClima.PRESSAO_MIN : 10,
    ColunaClima.RADIACAO : 10,
    ColunaClima.TEMP_AR : 10,
    ColunaClima.TEMP_ORVALHO : 10,
    ColunaClima.TEMP_MAX : 10,
    ColunaClima.TEMP_MIN : 10,
    ColunaClima.ORVALHO_MAX : 10,
    ColunaClima.ORVALHO_MIN : 10,
    ColunaClima.UMIDADE_MAX : 10,
    ColunaClima.UMIDADE_MIN : 10,
    ColunaClima.UMIDADE : 10,
    ColunaClima.VENTO_DIRECAO : 10,
    ColunaClima.VENTO_RAJADA : 10,
    ColunaClima.VENTO_VELOCIDADE : 10,
}