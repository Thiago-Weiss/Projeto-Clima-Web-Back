from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from datetime import date
from app.services.graficos import gerar_dados_grafico, gerar_dados_grafico_dia_mais
from app.core import Estados, ColunaClima, FiltroGraficoAgrupamento, DiaMais





router = APIRouter()

@router.get("/grafico")
def obter_dados_grafico(
    estado: Estados = Query(default= "Santa Catarina"),
    cidade: str = Query(default= "São José"),
    data_inicio: date = Query(default="2023-01-01", description= "Data no formato YYYY-MM-DD"),
    data_fim: date = Query(default="2023-12-31", description= "Data no formato YYYY-MM-DD"),
    colunas: list[ColunaClima] = Query(default= ["precipitacao"], description= "Nomes das colunas a serem filtradas"),
    agrupamentos: list[FiltroGraficoAgrupamento] = Query(default= ["sum_dia"], description= "Modos de agrupamento por dia"),
    hora_fixa: list[int] = Query(default= [10], description= "Hora fixa do agrupamento"),
    janela_hora_inicio: list[int] = Query(default= [10], description= "Janela hora inicio"),
    janela_hora_fim: list[int] = Query(default= [18], description= "Janela hora fim"),
):


    try:
        resultado = gerar_dados_grafico(
            estado= estado.value,
            cidade= cidade,
            data_inicio= data_inicio,
            data_fim= data_fim,
            colunas=colunas,
            agrupamentos= agrupamentos,
            hora_fixa= hora_fixa,
            janela_hora_inicio= janela_hora_inicio,
            janela_hora_fim= janela_hora_fim,
        )
        return JSONResponse(content= resultado)

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Erro interno: {str(e)}"})




@router.get("/grafico/dia-mais")
def obter_dados_grafico(
    estado: Estados = Query(default= "Santa Catarina"),
    cidade: str = Query(default= "São José"),
    data_inicio: date = Query(default="2023-01-01", description= "Data no formato YYYY-MM-DD"),
    data_fim: date = Query(default="2023-12-31", description= "Data no formato YYYY-MM-DD"),
    modo_dia: DiaMais = Query(default= "dia_max", description= "Filtro para ser usado no dia mais para o primeira coluna passada"),
    colunas: list[ColunaClima] = Query(default= ["precipitacao"], description= "Nomes das colunas a serem filtradas"),
    agrupamentos: list[FiltroGraficoAgrupamento] = Query(default= ["sum_dia"], description= "Modos de agrupamento por dia"),
    hora_fixa: list[int] = Query(default= [10], description= "Hora fixa do agrupamento"),
    janela_hora_inicio: list[int] = Query(default= [10], description= "Janela hora inicio"),
    janela_hora_fim: list[int] = Query(default= [18], description= "Janela hora fim"),
    dias_marge : int = Query(default= 1, description= "Quantos dias antes e depois do dia mais vai retornar junto", ge= 1, le= 7)
):
    try:
        resultado = gerar_dados_grafico_dia_mais(
            estado= estado.value,
            cidade= cidade,
            data_inicio= data_inicio,
            data_fim= data_fim,
            modo_dia = modo_dia,
            colunas= colunas,
            agrupamentos= agrupamentos,
            hora_fixa= hora_fixa,
            janela_hora_inicio= janela_hora_inicio,
            janela_hora_fim= janela_hora_fim,
            dias_marge= dias_marge
        )

        return JSONResponse(content= resultado)

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Erro interno: {str(e)}"})
