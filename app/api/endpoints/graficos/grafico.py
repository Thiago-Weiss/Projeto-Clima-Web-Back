from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from datetime import date

from app.services.graficos import gerar_dados_grafico
from app.core import Estados, ColunaClima, FiltroGraficoAgrupamento, RespostaFormato





router = APIRouter()

@router.get("/grafico")
def obter_dados_grafico(
    estado: Estados     = Query(default= "Santa Catarina", description= "OBRIGATÓRIO"),
    cidade: str         = Query(default= "São José",  description= "OBRIGATÓRIO"),
    data_inicio: date   = Query(default="2023-01-01", description= "OBRIGATÓRIO | Data no formato YYYY-MM-DD"),
    data_fim: date      = Query(default="2023-12-31", description= "OBRIGATÓRIO | Data no formato YYYY-MM-DD"),

    resposta_formato : RespostaFormato = Query(default="objeto", description= "Formatacao dos dados na resposta"),

    colunas: list[ColunaClima]                      = Query(description= "OBRIGATÓRIO | Nomes das colunas a serem filtradas"),
    agrupamentos: list[FiltroGraficoAgrupamento]    = Query(default=[], description= "Modos de agrupamento por dia"),
    hora_fixa: list[int]                            = Query(default=[], description= "Hora fixa do agrupamento"),
    janela_hora_inicio: list[int]                   = Query(default=[], description= "Janela hora inicio"),
    janela_hora_fim: list[int]                      = Query(default=[], description= "Janela hora fim"),

    dados_agrupados_por_x_dias: int = Query(default= 1, ge=1, le= 90, description= "Agrupa os dados/dias para gerar menos pontos pra grandes consultas"),

    auto_completar_colunas : bool = Query(default= True, description= "Nao validar os parametros para as colunas e auto-completar elas"),
):


    try:
        resultado = gerar_dados_grafico(
            estado= estado.value,
            cidade= cidade,
            data_inicio= data_inicio,
            data_fim= data_fim,
            resposta_formato = resposta_formato,
            colunas=colunas,
            agrupamentos= agrupamentos,
            hora_fixa= hora_fixa,
            janela_hora_inicio= janela_hora_inicio,
            janela_hora_fim= janela_hora_fim,
            dados_agrupados_por_x_dias = dados_agrupados_por_x_dias,
            auto_completar_colunas = auto_completar_colunas,
        )
        return JSONResponse(content= resultado)

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Erro interno: {str(e)}"})


