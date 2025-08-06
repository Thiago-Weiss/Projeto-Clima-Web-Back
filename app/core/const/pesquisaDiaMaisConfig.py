from app.core import PesquisaDiaMaisOpcoes, ColunaClima, FiltroGraficoAgrupamento, GraficoColunaConfig





PESQUISA_DIA_MAIS_CONFIGS = {
    PesquisaDiaMaisOpcoes.CHUVA : [
        GraficoColunaConfig(
            coluna= ColunaClima.PRECIPITACAO,
            modo_agrupamento= FiltroGraficoAgrupamento.SUM_DIA,
        )],

    PesquisaDiaMaisOpcoes.MAIOR_TEMPERATURA : [
        GraficoColunaConfig(
            coluna= ColunaClima.TEMP_AR,
            modo_agrupamento= FiltroGraficoAgrupamento.MAX_DIA,
        ),
        GraficoColunaConfig(
            coluna= ColunaClima.TEMP_MAX,
            modo_agrupamento= FiltroGraficoAgrupamento.MAX_DIA,
        ),
        GraficoColunaConfig(
            coluna= ColunaClima.TEMP_MIN,
            modo_agrupamento= FiltroGraficoAgrupamento.MAX_DIA,
        )],


    PesquisaDiaMaisOpcoes.MENOR_TEMPERATURA : [
        GraficoColunaConfig(
            coluna= ColunaClima.TEMP_AR,
            modo_agrupamento= FiltroGraficoAgrupamento.MIN_DIA,
        ),
        GraficoColunaConfig(
            coluna= ColunaClima.TEMP_MAX,
            modo_agrupamento= FiltroGraficoAgrupamento.MIN_DIA,
        ),
        GraficoColunaConfig(
            coluna= ColunaClima.TEMP_MIN,
            modo_agrupamento= FiltroGraficoAgrupamento.MIN_DIA,
        )],


}



