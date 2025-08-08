from enum import Enum
from app.core.const.clima import MAX_DIA, MIN_DIA, SUM_DIA, MEAN_DIA, HORA_FIXA, HORA_MIN_JANELA, HORA_MAX_JANELA, HORA_MEAN_JANELA, VARIACAO, VARIACAO_JANELA

class FiltroGraficoAgrupamento(str, Enum):
    MAX_DIA             = MAX_DIA
    MIN_DIA             = MIN_DIA
    SUM_DIA             = SUM_DIA
    MEAN_DIA            = MEAN_DIA
    HORA_FIXA           = HORA_FIXA
    HORA_MIN_JANELA     = HORA_MIN_JANELA
    HORA_MAX_JANELA     = HORA_MAX_JANELA
    HORA_MEAN_JANELA    = HORA_MEAN_JANELA
    VARIACAO            = VARIACAO
    VARIACAO_JANELA     = VARIACAO_JANELA