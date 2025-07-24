from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
import pandas as pd

from app.core.arquivosPaths.estadosCidades import PARQUET_FILE, COLUNA_ESTADO, COLUNA_CIDADE


router = APIRouter()

@router.get("/cidades")
def obter_cidades_por_estado(estado: str = Query(..., description="Sigla do estado, ex: SP")):

    df = pd.read_parquet(PARQUET_FILE)
    sc_row = df[df[COLUNA_ESTADO] == estado]

    if not sc_row.empty:
        cidades = sc_row[COLUNA_CIDADE].values[0]
        cidades = list(map(str, cidades))
        return JSONResponse(content= cidades)

    return JSONResponse(content=["Municipio não encontrado"])
