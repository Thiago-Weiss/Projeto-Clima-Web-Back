from app.core import EstacaoInfo
from app.core.const.respostasFront import ESTACAO_NOME, ESTACAO_CODIGO, ANO_INICIO, ANO_FIM, LATITUDE, LONGITUDE, ALTITUDE


def pegar_dados_das_estacoes_pesquisadas(estacoes : list[EstacaoInfo]):
    dados = []

    estacao_nome = estacoes[0].estacao_nome
    codigo = estacoes[0].codigo
    ano_inicio = estacoes[0].ano
    latitude = estacoes[0].latitude
    longitude = estacoes[0].longitude
    altitude = estacoes[0].altitude


    for estacao in estacoes:
        nome_atual = estacao.estacao_nome
        if nome_atual != estacao_nome:
            dados.append({
                ESTACAO_NOME: estacao_nome,
                ESTACAO_CODIGO: codigo,
                ANO_INICIO : ano_inicio,
                ANO_FIM : estacao.ano,
                LATITUDE: latitude,
                LONGITUDE: longitude,
                ALTITUDE: altitude,
            })
            estacao_nome = estacao.estacao_nome
            codigo = estacao.codigo
            ano_inicio = estacao.ano
            latitude = estacao.latitude
            longitude = estacao.longitude
            altitude = estacao.altitude

    dados.append({
        ESTACAO_NOME: estacao_nome,
        ESTACAO_CODIGO: codigo,
        ANO_INICIO : ano_inicio,
        ANO_FIM : estacoes[-1].ano,
        LATITUDE: latitude,
        LONGITUDE: longitude,
        ALTITUDE: altitude,
    })

    return dados
