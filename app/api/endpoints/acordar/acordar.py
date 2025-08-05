from fastapi import APIRouter

router = APIRouter()

@router.get("/acordar")
def obter_cidades_por_estado():
    return "só mais 5 min, mae"
