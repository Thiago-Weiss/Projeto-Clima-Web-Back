from dataclasses import dataclass

@dataclass
class EstacaoInfo:
    arquivo: str
    latitude: float
    longitude: float
    estacao: str
