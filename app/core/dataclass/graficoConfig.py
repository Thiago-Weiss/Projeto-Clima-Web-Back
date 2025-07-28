from dataclasses import dataclass
from typing import Tuple

from app.core import ColunaClima, FiltroGraficoAgrupamento



@dataclass
class GraficoColunaConfig:
    coluna: ColunaClima
    filtro: FiltroGraficoAgrupamento
    hora_fixa: int
    janela_horas: Tuple[int, int]
    