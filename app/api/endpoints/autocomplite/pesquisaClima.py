from fastapi import APIRouter, Query



from app.core.const.clima import COLUNAS_PESQUISA_SIMPLES, COLUNAS_PESQUISA_AVANCADA, MODO_AGRUPAMENTO_PESQUISA

router = APIRouter()

@router.get("/colunas-clima-simples")
def obter_colunas_clima_simples(descricao : bool = Query(default= False, description= "Retorna a descricao")):
    if descricao:
        return {val: COLUNAS_PESQUISA_SIMPLES[val] for val in COLUNAS_PESQUISA_SIMPLES}
    return list(COLUNAS_PESQUISA_SIMPLES.keys())
    



@router.get("/colunas-clima-avancada")
def obter_colunas_clima_avancado(descricao : bool = Query(default= False, description= "Retorna a descricao")):
    if descricao:
        return {val: COLUNAS_PESQUISA_AVANCADA[val] for val in COLUNAS_PESQUISA_AVANCADA}
    return list(COLUNAS_PESQUISA_AVANCADA.keys())


@router.get("/modo-de-agrupamento")
def obter_modos_de_agrupamento(descricao : bool = Query(default= False, description= "Retorna a descricao")):
    if descricao:
        return {val: MODO_AGRUPAMENTO_PESQUISA[val] for val in MODO_AGRUPAMENTO_PESQUISA}
    return list(MODO_AGRUPAMENTO_PESQUISA.keys())
    