from dataclasses import dataclass

from app.core import ColunaClima, FiltroGraficoAgrupamento



@dataclass
class GraficoColunaConfig:
    coluna: ColunaClima
    modo_agrupamento: FiltroGraficoAgrupamento
    hora_fixa: int = 0
    hora_janela_inicio: int = 0
    hora_janela_fim: int = 0
    