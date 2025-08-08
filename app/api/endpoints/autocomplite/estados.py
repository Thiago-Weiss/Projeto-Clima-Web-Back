from fastapi import APIRouter
from fastapi.responses import JSONResponse
import pandas as pd

from app.core.const.estadosCidades import PARQUET_FILE_CIDADES_ESTADOS, COLUNA_ESTADO

router = APIRouter()

@router.get("/estados",
            summary= "Lista os estados Brasileiros", 
            description= "Retorna uma lista dos estados Brasileiros")
def obter_estados():
    df = pd.read_parquet(PARQUET_FILE_CIDADES_ESTADOS, columns=[COLUNA_ESTADO])
    estados = df[COLUNA_ESTADO].dropna().unique().tolist()
    return JSONResponse(content= estados)
