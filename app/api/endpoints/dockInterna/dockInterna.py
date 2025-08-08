
from fastapi import APIRouter

router = APIRouter()


@router.get("/dock_interna")
def dock_interna():
    return {
        "origem_dos_dados": {
            "descricao": "Dados coletados do Instituto Nacional de Meteorologia (INMET) em formato tabular com 24 medições por dia do ano inteiro.",
            "periodo": "2000 até 08/2025, possivelmente mais atualizados.",
            "tratamento": "Remoção de valores impossíveis (chuva negativa, temperatura acima de 200°C, etc.). Não é feita previsão para dados faltantes."
        },
        "variaveis_climaticas": [
            {
                "nome": "PRECIPITAÇÃO TOTAL, HORÁRIA (mm)",
                "banco": "precipitacao",
                "descricao": "Quantidade de chuva medida no período de 1 hora, em milímetros.",
                "exemplo": "5.0 mm = 5 litros por m² naquela hora."
            },
            {
                "nome": "PRESSÃO ATMOSFÉRICA AO NÍVEL DA ESTAÇÃO, HORÁRIA (mB ou hPa)",
                "banco": "pressao",
                "descricao": "Pressão do ar na altitude da estação. Unidade: milibar (mB) ou hectopascal (hPa)."
            },
            {
                "nome": "PRESSÃO ATMOSFÉRICA MÁX. NA HORA ANT. (mB)",
                "banco": "pressao_max",
                "descricao": "Maior pressão atmosférica registrada na hora anterior."
            },
            {
                "nome": "PRESSÃO ATMOSFÉRICA MÍN. NA HORA ANT. (mB)",
                "banco": "pressao_min",
                "descricao": "Menor pressão atmosférica registrada na hora anterior."
            },
            {
                "nome": "RADIAÇÃO GLOBAL (KJ/m²)",
                "banco": "radiacao",
                "descricao": "Energia solar recebida por m² (em quilojoules). Importante para estudos climáticos, agricultura e energia solar."
            },
            {
                "nome": "TEMPERATURA DO AR – BULBO SECO, HORÁRIA (°C)",
                "banco": "temp_ar",
                "descricao": "Temperatura do ar no abrigo meteorológico. É a temperatura padrão usada em previsões."
            },
            {
                "nome": "TEMPERATURA DO PONTO DE ORVALHO (°C)",
                "banco": "temp_orvalho",
                "descricao": "Temperatura em que o ar atinge 100% de umidade e o orvalho se forma."
            },
            {
                "nome": "TEMPERATURA MÁXIMA NA HORA ANT. (°C)",
                "banco": "temp_max",
                "descricao": "Maior temperatura registrada na hora anterior."
            },
            {
                "nome": "TEMPERATURA MÍNIMA NA HORA ANT. (°C)",
                "banco": "temp_min",
                "descricao": "Menor temperatura registrada na hora anterior."
            },
            {
                "nome": "TEMPERATURA ORVALHO MÁX. NA HORA ANT. (°C)",
                "banco": "orvalho_max",
                "descricao": "Maior ponto de orvalho na hora anterior."
            },
            {
                "nome": "TEMPERATURA ORVALHO MÍN. NA HORA ANT. (°C)",
                "banco": "orvalho_min",
                "descricao": "Menor ponto de orvalho na hora anterior."
            },
            {
                "nome": "UMIDADE REL. MÁX. NA HORA ANT. (%)",
                "banco": "umidade_max",
                "descricao": "Maior umidade relativa registrada na hora anterior."
            },
            {
                "nome": "UMIDADE REL. MÍN. NA HORA ANT. (%)",
                "banco": "umidade_min",
                "descricao": "Menor umidade relativa registrada na hora anterior."
            },
            {
                "nome": "UMIDADE RELATIVA DO AR, HORÁRIA (%)",
                "banco": "umidade",
                "descricao": "Percentual de umidade do ar no momento."
            },
            {
                "nome": "VENTO, DIREÇÃO HORÁRIA (°)",
                "banco": "vento_direcao",
                "descricao": "Direção de onde o vento vem (0°/360°=N, 90°=Leste, 180°=Sul, 270°=Oeste)."
            },
            {
                "nome": "VENTO, RAJADA MÁXIMA (m/s)",
                "banco": "vento_rajada",
                "descricao": "Velocidade da maior rajada na última hora."
            },
            {
                "nome": "VENTO, VELOCIDADE HORÁRIA (m/s)",
                "banco": "vento_velocidade",
                "descricao": "Velocidade média do vento naquela hora."
            }
        ],
        "agrupamento": {
            "descricao": "Por padrão, as pesquisas agrupam os dados por dia. É possível agrupar múltiplos dias para gerar gráficos mais resumidos."
        },
        "filtros_pesquisa_avancada": {
            "descricao": "Formas de agrupar as 24 medições do dia.",
            "tipos": {
                "max_dia": "Valor máximo do dia.",
                "min_dia": "Valor mínimo do dia.",
                "sum_dia": "Soma de todos os valores do dia.",
                "mean_dia": "Média dos valores do dia."
            },
            "parametros_adicionais": {
                "hora_fixa": "Pega o valor da hora especificada.",
                "hora_min_janela": "Pega o valor mínimo dentro da janela de horas especificada.",
                "hora_max_janela": "Pega o valor máximo dentro da janela de horas especificada.",
                "hora_mean_janela": "Calcula a média dentro da janela de horas especificada."
            }
        }
    }