from fastapi import APIRouter



from app.core.const.clima import COLUNAS_PADRAO, DATA, HORA

router = APIRouter()

@router.get("/colunas-clima")
def obter_estados():
    colunas = [item for item in COLUNAS_PADRAO if item not in [DATA, HORA]]
    return colunas
