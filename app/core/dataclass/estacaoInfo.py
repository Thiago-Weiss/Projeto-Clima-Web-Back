from dataclasses import dataclass

@dataclass
class EstacaoInfo:
    arquivo: str
    latitude: float
    longitude: float
    altitude: float
    estacao_nome: str
    codigo: str
    ano: int