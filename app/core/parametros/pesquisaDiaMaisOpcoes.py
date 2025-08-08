from enum import Enum

class PesquisaDiaMaisOpcoes(str, Enum):
    CHUVA                   = "chuva"
    MAIOR_TEMPERATURA       = "maior_temperatura"
    MENOR_TEMPERATURA       = "menor_temperatura"

