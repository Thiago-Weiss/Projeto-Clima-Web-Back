from enum import Enum


class RespostaFormato(str, Enum):
    LISTA = "lista"
    OBJETO = "objeto"
    LISTA_ALTERNATIVA = "lista_alternativa"
