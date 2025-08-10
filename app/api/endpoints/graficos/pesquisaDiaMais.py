from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from datetime import date

from app.services.graficos import gerar_dados_dia_mais
from app.core import Estados, RespostaFormato, PesquisaDiaMaisOpcoes



router = APIRouter()


@router.get("/grafico/dia-mais",
            summary= "Grafico do \"Dia Mais\"", 
            description= "Gera um grafico do \"Dia Mais (exp: dia mais quente, dia mais frio, dia mais chuvoso)\" de um perio de tempo, se nao for informado o perido ele ira buscar em todos os anos disponiveis")
def get_dia_mais(
    estado: Estados     = Query(..., example= "Santa Catarina"),
    cidade: str         = Query(..., example= "São José"),
    data_inicio: date   = Query(default= "2000-01-01", description= "Data no formato YYYY-MM-DD"),
    data_fim: date      = Query(default= date.today(), description= "Data no formato YYYY-MM-DD"),
    
    coluna_climatica: PesquisaDiaMaisOpcoes = Query(description= "Nome da coluna a ser pesquisada"),

    dias_marge : int = Query(default= 3, description= "Quantos dias antes e depois do dia mais vai retornar junto", ge= 1, le= 7),
    resposta_formato : RespostaFormato = Query(default="objeto", description= "Formatacao dos dados na resposta"),
):
    try:
        resultado = gerar_dados_dia_mais(
            estado= estado.value,
            cidade= cidade,
            data_inicio= data_inicio,
            data_fim= data_fim,

            coluna_climatica = coluna_climatica,

            dias_marge= dias_marge,
            resposta_formato = resposta_formato,
        )

        return resultado

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Erro interno: {str(e)}"})
