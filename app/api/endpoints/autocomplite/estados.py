from fastapi import APIRouter
from fastapi.responses import JSONResponse
import pandas as pd

from app.core.const.estadosCidades import PARQUET_FILE, COLUNA_ESTADO

router = APIRouter()

@router.get("/estados")
def obter_estados():
    df = pd.read_parquet(PARQUET_FILE)
    estados = df[COLUNA_ESTADO].dropna().unique().tolist()
    return JSONResponse(content= estados)
