from app.core import  ColunaClima, FiltroGraficoAgrupamento, GraficoColunaConfig



def validar_grafico_coluna_config(
    colunas: list[ColunaClima],
    agrupamentos: list[FiltroGraficoAgrupamento],
    hora_fixa: list[int],
    janela_inicio: list[int],
    janela_fim: list[int]) -> list[GraficoColunaConfig] | str:
    
    print(colunas)
    print(agrupamentos)
    print(hora_fixa)
    print(janela_inicio)
    print(janela_fim)


    def validar_intervalo(valores: list[int], nome_lista: str):
        for val in valores:
            if not 0 <= val <= 23:
                return f"valor: {val} na lista: {nome_lista} está fora do limite de tempo"
        return None


    # 1️⃣ Checa duplicidade de colunas
    if len(colunas) != len(set(colunas)):
        return "Não pode ter colunas repetidas"

    # 2️⃣ Checa listas vazias
    if not hora_fixa:
        return "Parametro hora_fixa está vazio"
    if not janela_inicio:
        return "Parametro janela_inicio está vazio"
    if not janela_fim:
        return "Parametro janela_fim está vazio"


    # 3️⃣ Checa se todas as listas têm o mesmo tamanho
    tamanho = len(colunas)
    if not all(len(lst) == tamanho for lst in [agrupamentos, hora_fixa, janela_inicio, janela_fim]):
        return "As listas devem ter o mesmo tamanho"


    # 4️⃣ Valida intervalos de hora
    for lista, nome in [(hora_fixa, "hora_fixa"), (janela_inicio, "janela_inicio"), (janela_fim, "janela_fim")]:
        erro = validar_intervalo(lista, nome)
        if erro:
            return erro

    # 5️⃣ Valida se janela_inicio < janela_fim
    for i, (ini, fim) in enumerate(zip(janela_inicio, janela_fim)):
        if ini >= fim:
            return f"janela_inicio ({ini}) deve ser menor que janela_fim ({fim}) no índice {i}"



    # 6️⃣ Cria a lista de configurações
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