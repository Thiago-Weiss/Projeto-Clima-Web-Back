from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from app.services.graficos import gerar_dados_grafico

router = APIRouter()

@router.get("/grafico/dados")
def obter_dados_grafico(
    estado: str = Query(...),
    cidade: str = Query(...),
    data_inicio: str = Query(...),
    data_fim: str = Query(...),
    coluna: str = Query(...)
):
    try:
        resultado = gerar_dados_grafico(
            estado= estado,
            cidade= cidade,
            data_inicio= data_inicio,
            data_fim= data_fim,
            coluna= coluna
        )
        return JSONResponse(content= resultado)

    except ValueError as ve:
        return JSONResponse(status_code=400, content={"erro": str(ve)})

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Erro interno: {str(e)}"})
