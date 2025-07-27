from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from datetime import date
from app.services.graficos import gerar_dados_grafico, gerar_dados_dia_grafico
from app.core.enums import Estados


router = APIRouter()

@router.get("/grafico")
def obter_dados_grafico(
    estado: Estados = Query(...),
    cidade: str = Query(...),
    data_inicio: date = Query(..., description= "Data no formato YYYY-MM-DD", example="2023-01-01"),
    data_fim: date = Query(..., description= "Data no formato YYYY-MM-DD", example="2023-12-31"),
    coluna: str = Query(...)
):


    try:
        resultado = gerar_dados_grafico(
            estado= estado.value,
            cidade= cidade,
            data_inicio= data_inicio,
            data_fim= data_fim,
            coluna= coluna
        )
        return JSONResponse(content= resultado)

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Erro interno: {str(e)}"})




@router.get("/grafico/dia-mais")
def obter_dados_grafico(
    estado: Estados = Query(...),
    cidade: str = Query(...),
    data_inicio: date = Query(default= "2000-01-01", description= "Data no formato YYYY-MM-DD"),
    data_fim: date = Query(default= date.today(), description= "Data no formato YYYY-MM-DD"),
    coluna: str = Query(...)
):
    try:
        resultado = gerar_dados_dia_grafico(
            estado= estado.value,
            cidade= cidade,
            data_inicio= data_inicio,
            data_fim= data_fim,
            coluna= coluna
        )
        return JSONResponse(content= resultado)

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Erro interno: {str(e)}"})
