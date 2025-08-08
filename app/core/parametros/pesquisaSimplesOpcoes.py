from enum import Enum

class PesquisaSimplesOpcoes(str, Enum):
    CHUVA           = "chuva"
    UMIDADE         = "umidade"
    TEMPERATURA     = "temperatura"
    VENTO           = "vento"
