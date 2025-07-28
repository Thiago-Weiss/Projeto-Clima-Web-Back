from dataclasses import dataclass
from typing import Tuple

from app.core import ColunaClima, FiltroGraficoAgrupamento



@dataclass
class GraficoColunaConfig:
    coluna: ColunaClima
    modo_agrupamento: FiltroGraficoAgrupamento
    hora_fixa: int
    hora_janela_inicio: int
    hora_janela_fim: int