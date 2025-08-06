from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from datetime import date
from app.services.graficos import gerar_dados_pesquisa_simples
from app.core import Estados, PesquisaSimplesOpcoes, RespostaFormato





router = APIRouter()

@router.get("/grafico/pesquisa-simples")
def obter_dados_grafico(
    estado: Estados     = Query(..., example= "Santa Catarina", description= "OBRIGATÓRIO"),
    cidade: str         = Query(..., example= "São José",  description= "OBRIGATÓRIO"),
    data_inicio: date   = Query(..., example= "2023-01-01", description= "OBRIGATÓRIO | Data no formato YYYY-MM-DD"),
    data_fim: date      = Query(..., example= "2023-12-31", description= "OBRIGATÓRIO | Data no formato YYYY-MM-DD"),
    coluna_climatica: PesquisaSimplesOpcoes = Query(description= "Nome da coluna a ser pesquisada"),

    resposta_formato : RespostaFormato = Query(default= RespostaFormato.OBJETO, description= "Formatacao dos dados na resposta"),
    dados_agrupados_por_x_dias: int = Query(default= 1, ge=1, le= 90, description= "Agrupa os dados/dias para gerar menos pontos pra grandes consultas"),
):

    try:
        resultado = gerar_dados_pesquisa_simples(
            estado= estado.value,
            cidade= cidade,
            data_inicio= data_inicio,
            data_fim= data_fim,
            coluna_climatica= coluna_climatica,
            resposta_formato = resposta_formato,
            dados_agrupados_por_x_dias = dados_agrupados_por_x_dias,
        )
        return JSONResponse(content= resultado)

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Erro interno: {str(e)}"})



