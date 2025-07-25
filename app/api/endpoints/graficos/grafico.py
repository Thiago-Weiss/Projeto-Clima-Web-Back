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
    """
    estado          = tem que ser a string exata que é enviado no autocomplite para o front 
    cidade          = tem que ser a string exata que é enviado no autocomplite para o front 
    data_inicio     = formato YYYY-MM-DD
    data_fim        = formato YYYY-MM-DD

    coluna          = ainda falta fazer mais vai precisar de mais parametros pra montar ela mas vai ser algo assim
                    pra cada coluna do grafico

                    coluna= "precipitacao",     
                    filtro= "soma",        
                    hora_fixa= 23,                        
                    janela_horas= (10, 12)
                    
                    a coluna e o filtro vai ser passado por endpoits para o front ou talvez hard code pq sao constantes
                    e isso evitaria multiplos acessos ao back


    """


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
