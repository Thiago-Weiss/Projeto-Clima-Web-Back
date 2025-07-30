from datetime import datetime
from .basePath import DOWNLOAD_DIR_BASE, EXTRACT_DIR_BASE, PROCESSADOS_DIR_BASE


# url de download
URL_DOWNLOAD = 'https://portal.inmet.gov.br/uploads/dadoshistoricos/'


# processamento do arquivo (dir e files)
SUB_DIR = "clima"

# download
ZIP_DIR = DOWNLOAD_DIR_BASE / SUB_DIR

# extraido
EXTRACT_DIR = EXTRACT_DIR_BASE / SUB_DIR

# salvo o arquivo final
PARQUET_DIR =  PROCESSADOS_DIR_BASE / SUB_DIR



# ano dos arquivos
ANO_INICIO   = 2000
ANO_FINAL = datetime.now().year




# colunas da tabela
DATA                = "data"
HORA                = "hora"
PRECIPITACAO        = "precipitacao"
PRESSAO             = "pressao"
PRESSAO_MAX         = "pressao_max"
PRESSAO_MIN         = "pressao_min"
RADIACAO            = "radiacao"
TEMP_AR             = "temp_ar"
TEMP_ORVALHO        = "temp_orvalho"
TEMP_MAX            = "temp_max"
TEMP_MIN            = "temp_min"
ORVALHO_MAX         = "orvalho_max"
ORVALHO_MIN         = "orvalho_min"
UMIDADE_MAX         = "umidade_max"
UMIDADE_MIN         = "umidade_min"
UMIDADE             = "umidade"
VENTO_DIRECAO       = "vento_direcao"
VENTO_RAJADA        = "vento_rajada"
VENTO_VELOCIDADE    = "vento_velocidade"

# Lista com todas as colunas na ordem
COLUNAS_PADRAO = [
    DATA,
    HORA,
    PRECIPITACAO,
    PRESSAO,
    PRESSAO_MAX,
    PRESSAO_MIN,
    RADIACAO,
    TEMP_AR,
    TEMP_ORVALHO,
    TEMP_MAX,
    TEMP_MIN,
    ORVALHO_MAX,
    ORVALHO_MIN,
    UMIDADE_MAX,
    UMIDADE_MIN,
    UMIDADE,
    VENTO_DIRECAO,
    VENTO_RAJADA,
    VENTO_VELOCIDADE
]



VALOR_ALTURA_NULA = -9999



COLUNAS_PESQUISA_AVANCADA ={
    PRECIPITACAO : "Quantidade de chuva medida no período em milímetros.",
    PRESSAO : "Medida da pressão do ar na altitude onde a estação está localizada.",
    PRESSAO_MAX : "A maior pressão atmosférica registrada pela estação na hora anterior.",
    PRESSAO_MIN : "A menor pressão atmosférica registrada pela estação na hora anterior.",
    RADIACAO : "Quantidade de energia solar recebida por metro quadrado, medida em quilojoules por metro quadrado.",
    TEMP_AR : "A temperatura do ar “normal” registrada no abrigo meteorológico.",
    TEMP_ORVALHO : "Temperatura em que o ar se torna saturado de umidade (100% de umidade relativa) e o orvalho começa a se formar.",
    TEMP_MAX : "A maior temperatura registrada pela estação na hora anterior.",
    TEMP_MIN : "A menor temperatura registrada pela estação na hora anterior.",
    ORVALHO_MAX : "O maior ponto de orvalho registrado pela estação na hora anterior.",
    ORVALHO_MIN : "O menor ponto de orvalho registrado pela estação na hora anterior.",
    UMIDADE_MAX : "A maior umidade relativa registrada na hora anterior.",
    UMIDADE_MIN : "A menor umidade relativa registrada na hora anterior.",
    UMIDADE : "Percentual de umidade do ar (quanto mais próximo de 100%, mais úmido).",
    VENTO_DIRECAO : "A direção de onde o vento vem, em graus (0° ou 360° = Norte, 90° = Leste, 180° = Sul, 270° = Oeste).",
    VENTO_RAJADA : "Velocidade da maior rajada de vento registrada na última hora.",
    VENTO_VELOCIDADE : "Velocidade média do vento naquela hora."
}


COLUNAS_PESQUISA_SIMPLES = {
    PRECIPITACAO : "Quantidade de chuva medida no período em milímetros.",
    PRESSAO : "Medida da pressão do ar na altitude onde a estação está localizada.",
    RADIACAO : "Quantidade de energia solar recebida por metro quadrado, medida em quilojoules por metro quadrado.",
    TEMP_AR : "A temperatura do ar “normal” registrada no abrigo meteorológico.",
    TEMP_ORVALHO : "Temperatura em que o ar se torna saturado de umidade (100% de umidade relativa) e o orvalho começa a se formar.",
    UMIDADE : "Percentual de umidade do ar (quanto mais próximo de 100%, mais úmido).",
    VENTO_DIRECAO : "A direção de onde o vento vem, em graus (0° ou 360° = Norte, 90° = Leste, 180° = Sul, 270° = Oeste).",
    VENTO_VELOCIDADE : "Velocidade média do vento naquela hora."
}






MAX_DIA             = "max_dia"
MIN_DIA             = "min_dia"
SUM_DIA             = "sum_dia"
MEAN_DIA            = "mean_dia"
HORA_FIXA           = "hora_fixa"
HORA_MIN_JANELA     = "hora_min_janela"
HORA_MAX_JANELA     = "hora_max_janela"
HORA_MEAN_JANELA    = "hora_mean_janela"
VARIACAO            = "variacao"
VARIACAO_JANELA     = "variacao_janela"

MODO_AGRUPAMENTO_PESQUISA = {
    MAX_DIA: "Agrupa pelo valor máximo do dia (ex: temperatura máxima)",
    MIN_DIA: "Agrupa pelo valor mínimo do dia (ex: temperatura mínima)",
    SUM_DIA: "Agrupa somando os valores do período (ex: precipitação total)",
    MEAN_DIA: "Agrupa pela média diária dos valores (ex: umidade média)",
    HORA_FIXA: "Usa o valor exato de uma hora específica",
    HORA_MIN_JANELA: "Agrupa pelo menor valor dentro de uma janela de tempo",
    HORA_MAX_JANELA: "Agrupa pelo maior valor dentro de uma janela de tempo",
    HORA_MEAN_JANELA: "Agrupa pela média dos valores dentro de uma janela de tempo",
    VARIACAO: "Agrupa calculando a variação entre valores (ex: diferença de temperatura)",
    VARIACAO_JANELA: "Agrupa pela variação dentro de uma janela de tempo",
}














