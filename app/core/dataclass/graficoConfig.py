from dataclasses import dataclass
from typing import Tuple

from app.core.enums import ColunaClima, FiltroGrafico




@dataclass
class GraficoColunaConfig:
    coluna: ColunaClima
    filtro: FiltroGrafico
    hora_fixa: int
    janela_horas: Tuple[int, int]
    