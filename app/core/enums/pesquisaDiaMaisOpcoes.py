from enum import Enum

class PesquisaDiaMaisOpcoes(str, Enum):
    CHUVA                   = "CHUVA"
    MAIOR_TEMPERATURA       = "MAIOR_TEMPERATURA"
    MENOR_TEMPERATURA       = "MENOR_TEMPERATURA"

