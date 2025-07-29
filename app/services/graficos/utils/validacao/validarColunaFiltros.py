from app.core import  ColunaClima, FiltroGraficoAgrupamento, GraficoColunaConfig
from app.core.const.filtroValoresPadrao import MODO_AGRUPAMENTO, HORA_FIXA, HORA_JANELA_INICIO, HORA_JANELA_FIM


def validar_grafico_coluna_config(
    colunas: list[ColunaClima],
    agrupamentos: list[FiltroGraficoAgrupamento],
    hora_fixa: list[int],
    janela_inicio: list[int],
    janela_fim: list[int],
    auto_completar : bool = True) -> list[GraficoColunaConfig] | list[str]:
    

    erros : list[str] = []

    def validar_intervalo(valores: list[int], nome_lista: str):
        for val in valores:
            if not 0 <= val <= 23:
                erros.append(f"{len(erros)} Erro - Valor: {val} na lista: {nome_lista} está fora do limite de tempo")



    # 1️⃣ Checa duplicidade de colunas
    if len(colunas) != len(set(colunas)):
        erros.append(f"{len(erros)} Erro - Não pode ter colunas repetidas")

    # 2️⃣ Checa listas vazias
    if not hora_fixa:
        erros.append(f"{len(erros)} Erro - Parametro hora_fixa está vazio")
    if not janela_inicio:
        erros.append(f"{len(erros)} Erro - Parametro janela_inicio está vazio")
    if not janela_fim:
        erros.append(f"{len(erros)} Erro - Parametro janela_fim está vazio")


    # 3️⃣ Checa se todas as listas têm o mesmo tamanho e se nao passou do limite de colunas por requisicao
    tamanho = len(colunas)
    limite_colunas = 5
    if not all(len(lst) == tamanho for lst in [agrupamentos, hora_fixa, janela_inicio, janela_fim]):
        erros.append(f"{len(erros)} Erro - As listas devem ter o mesmo tamanho")
    if tamanho > limite_colunas:
        erros.append(f"{len(erros)} Erro - Maximo de colunas por requisicao é {limite_colunas}")

    # 4️⃣ Valida intervalos de hora
    for lista, nome in [(hora_fixa, "hora_fixa"), (janela_inicio, "janela_inicio"), (janela_fim, "janela_fim")]:
        validar_intervalo(lista, nome)


    # 5️⃣ Valida se janela_inicio < janela_fim
    for i, (ini, fim) in enumerate(zip(janela_inicio, janela_fim)):
        if ini >= fim:
            erros.append(f"{len(erros)} Erro - janela_inicio ({ini}) deve ser menor que janela_fim ({fim}) no índice {i}")


    # tem erros
    if erros:
        # retorna os erros
        if not auto_completar:
            return erros
        
        # se nao tiver nenhuma coluna retorna os erros tambem
        elif not colunas:
            return erros

        # tem erros mas gera os filtros padroes pra colunas
        else:
            filtros = []
            colunas = list(dict.fromkeys(colunas))[:limite_colunas]
            for coluna in colunas:
                filtros.append(
                    GraficoColunaConfig(
                        coluna= coluna,
                        modo_agrupamento= MODO_AGRUPAMENTO.get(coluna),
                        hora_fixa= HORA_FIXA.get(coluna),
                        hora_janela_inicio= HORA_JANELA_INICIO.get(coluna),
                        hora_janela_fim= HORA_JANELA_FIM.get(coluna)))
            return filtros


    # nao tem erros e gera os filtros normamentes
    filtros = [
        GraficoColunaConfig(
            coluna= col,
            modo_agrupamento= grp,
            hora_fixa= hf,
            hora_janela_inicio= ji,
            hora_janela_fim= jf
        )
        for col, grp, hf, ji, jf in zip(colunas, agrupamentos, hora_fixa, janela_inicio, janela_fim)
    ]

    return filtros