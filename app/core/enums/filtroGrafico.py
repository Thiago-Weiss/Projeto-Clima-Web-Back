from enum import Enum

class FiltroGrafico(Enum):
    MAX_DIA = 0
    MIN_DIA = 1
    SUM_DIA = 2
    MEAN_DIA = 3
    HORA_FIXA = 4
    HORA_MIN_JANELA = 5
    HORA_MAX_JANELA = 6
    HORA_MEAN_JANELA = 7