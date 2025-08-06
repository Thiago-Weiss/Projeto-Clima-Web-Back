from enum import Enum

class PesquisaSimplesOpcoes(str, Enum):
    CHUVA           = "CHUVA"
    UMIDADE         = "UMIDADE"
    TEMPERATURA     = "TEMPERATURA"
    VENTO           = "VENTO"
