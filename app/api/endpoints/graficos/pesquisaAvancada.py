from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from datetime import date

from app.services.graficos import gerar_dados_pesquisa_avancada
from app.core import Estados, ColunaClima, FiltroGraficoAgrupamento, RespostaFormato





router = APIRouter()

@router.get("/grafico/pesquisa-avancada",
            summary= "Grafico da pesquisa avançada", 
            description= "Gerar um grafico de até 5 variavies climaticas podendo configurar o processamento interno das variaveis climaticas. exp: sum_dia ira somar todos os valores do dia para gerar um ponto no grafico, max_dia ira pegar o ponto de valor numerico maior para ser o ponto do dia")
def get_pesquisa_avancada(
    estado: Estados     = Query(..., example= "Santa Catarina"),
    cidade: str         = Query(..., example= "São José"),
    data_inicio: date   = Query(..., example= "2023-01-01", description= "Data no formato YYYY-MM-DD"),
    data_fim: date      = Query(..., example= "2023-12-31", description= "Data no formato YYYY-MM-DD"),

    colunas: list[ColunaClima]                      = Query(description= "OBRIGATÓRIO | TEM QUE TER A MESMA QUANTIDAD DE ELESMENTOS (1 - 5) | Nomes das colunas a serem filtradas"),
    agrupamentos: list[FiltroGraficoAgrupamento]    = Query(description= "OBRIGATÓRIO | TEM QUE TER A MESMA QUANTIDAD DE ELESMENTOS (1 - 5) | Modos de agrupamento por dia"),
    hora_fixa: list[int]                            = Query(description= "OBRIGATÓRIO | TEM QUE TER A MESMA QUANTIDAD DE ELESMENTOS (1 - 5) | Hora fixa do agrupamento"),
    janela_hora_inicio: list[int]                   = Query(description= "OBRIGATÓRIO | TEM QUE TER A MESMA QUANTIDAD DE ELESMENTOS (1 - 5) | Janela hora inicio"),
    janela_hora_fim: list[int]                      = Query(description= "OBRIGATÓRIO | TEM QUE TER A MESMA QUANTIDAD DE ELESMENTOS (1 - 5) | Janela hora fim"),

    dados_agrupados_por_x_dias: int = Query(default= 1, ge=1, le= 30, description= "Agrupa os dados/dias para gerar menos pontos pra grandes consultas"),
    resposta_formato : RespostaFormato = Query(default= RespostaFormato.OBJETO, description= "Formatacao dos dados na resposta"),
):


    try:
        resultado = gerar_dados_pesquisa_avancada(
            estado= estado.value,
            cidade= cidade,
            data_inicio= data_inicio,
            data_fim= data_fim,

            colunas=colunas,
            agrupamentos= agrupamentos,
            hora_fixa= hora_fixa,
            janela_hora_inicio= janela_hora_inicio,
            janela_hora_fim= janela_hora_fim,

            dados_agrupados_por_x_dias = dados_agrupados_por_x_dias,
            resposta_formato = resposta_formato,
        )
        return resultado

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Erro interno: {str(e)}"})

