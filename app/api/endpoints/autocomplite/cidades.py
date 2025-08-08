from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
import pandas as pd

from app.core.const.estadosCidades import PARQUET_FILE_CIDADES_ESTADOS, COLUNA_ESTADO, COLUNA_CIDADE
from app.core import Estados

router = APIRouter()

@router.get("/cidades",            
            summary= "Lista as cidades de um estado", 
            description= "Retorna uma lista das cidades do estado informado")
def obter_cidades_por_estado(estado: Estados = Query(...)):

    df = pd.read_parquet(PARQUET_FILE_CIDADES_ESTADOS, columns=[COLUNA_ESTADO, COLUNA_CIDADE])
    sc_row = df[df[COLUNA_ESTADO] == estado]

    if not sc_row.empty:
        cidades = sc_row[COLUNA_CIDADE].tolist()
        return JSONResponse(content= cidades)

    return JSONResponse(content=["Municipio não encontrado"])
