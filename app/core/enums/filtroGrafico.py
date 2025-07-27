from enum import Enum


class FiltroGraficoAgrupamento(str, Enum):
    MAX_DIA             = "max_dia"
    MIN_DIA             = "min_dia"
    SUM_DIA             = "sum_dia"
    MEAN_DIA            = "mean_dia"
    HORA_FIXA           = "hora_fixa"
    HORA_MIN_JANELA     = "hora_min_janela"
    HORA_MAX_JANELA     = "hora_max_janela"
    HORA_MEAN_JANELA    = "hora_mean_janela"
    VARIACAO            = "variacao"
    VARIACAO_JANELA     = "variacao_janela"