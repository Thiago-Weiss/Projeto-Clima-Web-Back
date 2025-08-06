from app.core import PesquisaSimplesOpcoes, ColunaClima, FiltroGraficoAgrupamento, GraficoColunaConfig





PESQUISA_SIMPLES_CONFIGS = {
    PesquisaSimplesOpcoes.CHUVA : [
        GraficoColunaConfig(
            coluna= ColunaClima.PRECIPITACAO,
            modo_agrupamento= FiltroGraficoAgrupamento.SUM_DIA,
        )],

    PesquisaSimplesOpcoes.TEMPERATURA : [
        GraficoColunaConfig(
            coluna= ColunaClima.TEMP_AR,
            modo_agrupamento= FiltroGraficoAgrupamento.MEAN_DIA,
        ),
        GraficoColunaConfig(
            coluna= ColunaClima.TEMP_MAX,
            modo_agrupamento= FiltroGraficoAgrupamento.MAX_DIA,
        ),
        GraficoColunaConfig(
            coluna= ColunaClima.TEMP_MIN,
            modo_agrupamento= FiltroGraficoAgrupamento.MIN_DIA,
        )],


    PesquisaSimplesOpcoes.UMIDADE : [
        GraficoColunaConfig(
            coluna= ColunaClima.UMIDADE,
            modo_agrupamento= FiltroGraficoAgrupamento.MEAN_DIA,
        ),
        GraficoColunaConfig(
            coluna= ColunaClima.UMIDADE_MAX,
            modo_agrupamento= FiltroGraficoAgrupamento.MAX_DIA,
        ),
        GraficoColunaConfig(
            coluna= ColunaClima.UMIDADE_MIN,
            modo_agrupamento= FiltroGraficoAgrupamento.MIN_DIA,
        )],

    PesquisaSimplesOpcoes.VENTO : [GraficoColunaConfig(
        coluna= ColunaClima.VENTO_VELOCIDADE,
        modo_agrupamento= FiltroGraficoAgrupamento.MAX_DIA,
    )],
}



