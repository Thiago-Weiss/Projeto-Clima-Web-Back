from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
import pandas as pd

from app.core.const.estadosCidades import PARQUET_FILE_CIDADES_ESTADOS, COLUNA_ESTADO, COLUNA_CIDADE
from app.core import Estados

router = APIRouter()

@router.get("/cidades")
def obter_cidades_por_estado(estado: Estados = Query(...)):

    df = pd.read_parquet(PARQUET_FILE_CIDADES_ESTADOS)
    sc_row = df[df[COLUNA_ESTADO] == estado]

    if not sc_row.empty:
        cidades = sc_row[COLUNA_CIDADE].values[0]
        cidades = list(map(str, cidades))
        return JSONResponse(content= cidades)

    return JSONResponse(content=["Municipio não encontrado"])
