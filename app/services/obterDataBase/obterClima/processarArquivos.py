from os import makedirs, path, listdir
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
import numpy as np 
from queue import Queue

from app.core.const.clima import *
from app.core.const.index import *



# Config
OUTPUT_DIR = PARQUET_DIR
INDEX_DIR = INDEX_DIR

# Dicionário para renomeação das colunas
COLUNAS_PADRAO = COLUNAS_PADRAO



# validacao dos dados do DF
def validar_e_limpar_dados(df: pd.DataFrame) -> pd.DataFrame:
    # transforma tudo pra numero pra armazenar no parquet
    colunas_numericas = [
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
        VENTO_VELOCIDADE]
    
    for col in colunas_numericas:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col])


    # Umidade Relativa
    valorMin = 0
    valorMax = 100
    df.loc[(df[UMIDADE] < valorMin) | (df[UMIDADE] > valorMax), UMIDADE] = np.nan
    df.loc[(df[UMIDADE_MAX] < valorMin) | (df[UMIDADE_MAX] > valorMax), UMIDADE_MAX] = np.nan
    df.loc[(df[UMIDADE_MIN] < valorMin) | (df[UMIDADE_MIN] > valorMax), UMIDADE_MIN] = np.nan

    # Temperaturas
    limiteTempMin = -100
    limiteTempMax = 100
    colunasTemperatura = [
        TEMP_AR, TEMP_MAX, TEMP_MIN,
        TEMP_ORVALHO, ORVALHO_MAX, ORVALHO_MIN
    ]
    for col in colunasTemperatura:
        if col in df.columns:
            df.loc[(df[col] < limiteTempMin) | (df[col] > limiteTempMax), col] = np.nan

    # Valores que não podem ser negativos
    colunasPositivas = [
        VENTO_VELOCIDADE, VENTO_RAJADA,
        PRECIPITACAO, RADIACAO,
        PRESSAO, PRESSAO_MAX, PRESSAO_MIN
    ]
    for col in colunasPositivas:
        if col in df.columns:
            df.loc[df[col] < 0, col] = np.nan

    # Direção do vento
    if VENTO_DIRECAO in df.columns:
        df.loc[(df[VENTO_DIRECAO] < 0) | (df[VENTO_DIRECAO] > 360), VENTO_DIRECAO] = np.nan

    return df

# garante o df tenha os 24 pontos de todos os dias
def completar_datas_horas(df: pd.DataFrame, ano: int) -> pd.DataFrame:
    # garante que data seja do tipo datatime
    df[DATA] = pd.to_datetime(df[DATA])

    # gera todos os pontos para o ano pricipal
    inicio = pd.Timestamp(year=ano, month=1, day=1)
    fim = pd.Timestamp(year=ano, month=12, day=31)
    dias_ano = pd.date_range(inicio, fim, freq="D")
    horas = range(24)

    # index de todos os pontos
    grid_ano = pd.MultiIndex.from_product([dias_ano, horas], names=[DATA, HORA]).to_frame(index=False)

    # garante que o ano inteiro tenhas os 24 pontos por dia
    df_ano = grid_ano.merge(df, on=[DATA, HORA], how="left")



    # pega datas fora do ano atual como:o primeiro dia do proximo ano ou o ultimo da ano anterior
    datas_fora = df.loc[(df[DATA] < inicio) | (df[DATA] > fim), DATA].unique()

    # cira os 24 pontos para os dias fora do ano atual
    grids_extras = []
    for data_extra in datas_fora:
        # cria 24 horas pra esse dia
        grid_extra = pd.DataFrame({
            DATA: [data_extra] * 24,
            HORA: list(horas)
        })
        grids_extras.append(grid_extra)


    # se tiver dias fora do ano junta eles e prenche os dados se nao tiver cria um df vazio
    if grids_extras:
        grid_extras_df = pd.concat(grids_extras, ignore_index=True)
        df_extras = grid_extras_df.merge(df, on=[DATA, HORA], how="left")

    else:
        df_extras = pd.DataFrame(columns=df_ano.columns)


    # junta o df do ano atual com o dias a mais  se tiver 
    if not df_extras.empty:
        df_final = pd.concat([df_ano, df_extras], ignore_index=True)
    else:
        df_final = df_ano

    # reordena tudo
    df_final = df_final.sort_values(by=[DATA, HORA]).reset_index(drop=True)

    return df_final




# transforma a hora no padrao de inteiro de 00 a 23
def extrair_hora(horaStr):
    horaStr = str(horaStr).strip()

    if ":" in horaStr:
        # Formato 'HH:MM', ex: '02:00'
        try:
            return int(horaStr.split(":")[0])
        except:
            print(f"[❌] Erro em ao extrair a hora {horaStr}")
            return None
    else:
        # Formato 'HHMM UTC', ex: '0200 UTC'
        try:
            # remove ' UTC' se existir e pega só os 4 primeiros caracteres
            parteHora = horaStr.replace(" UTC", "")[:4]
            return int(parteHora[:2])
        except:
            print(f"[❌] Erro em ao extrair a hora {horaStr}")
            return None


# pega os valores pelo numero da linha por conta de diferença entre linhas
def extrair_meta_dados(linha):
    if not linha or ';' not in linha:
        return ''
    
    partes = linha.split(';')
    if len(partes) > 1:
        return partes[1].strip()
    return ''




def validar_df_percentual_dados(df: pd.DataFrame, csvPath, limiteMinPercentual= 0.10):
    # Pegar as colunas dos dados
    colunasDados = df.columns[2:]
    totalCelulas = df.shape[0] * len(colunasDados)

    # Contar quantos valores não nulos existem nas colunas de dados
    valoresValidos = df[colunasDados].notna().sum().sum()

    proporcao = valoresValidos / totalCelulas

    if proporcao < limiteMinPercentual:
        print(f"⚠️  DF Descartado, apenas {proporcao:.2%} de dados válidos. arquivo {csvPath}")
        return False
    return True


def validar_df_nao_vazios(df: pd.DataFrame, csvPath):
    # Pegar as colunas dos dados
    colunasDados = df.columns[2:]

    # Verifica se todas essas colunas estão completamente vazias
    if df[colunasDados].isna().all().all():
        print(f"⚠️  DF Descartado, todas as colunas de dados estão vazias. arquivo {csvPath}")
        return False
    return True



# processa os csv para paraquet
def processar_csv(dir):
    ano, pasta = dir
    # faz uma lista de todos os csv
    arquivosCSVs = [path.join(pasta, f) for f in listdir(pasta) if f.lower().endswith(".csv")]

    # faz o dir de saida
    makedirs(path.join(OUTPUT_DIR, str(ano)), exist_ok=True)
    
    # faz o path do index
    indexPath = path.join(INDEX_DIR, f"index{ano}.parquet")
    makedirs(path.dirname(indexPath), exist_ok=True)


    # o dados do index
    registrosIndex = []
    for csvPath in arquivosCSVs:
        try:
            with open(csvPath, 'r', encoding="ISO-8859-1") as f:
                # Lê as primeiras 8 linhas
                linhas = [next(f) for _ in range(8)]


            regiao = extrair_meta_dados(linhas[0]) 
            uf = extrair_meta_dados(linhas[1]) 
            estacao = extrair_meta_dados(linhas[2])
            codigo = extrair_meta_dados(linhas[3])
            latitude = extrair_meta_dados(linhas[4]).replace(',', '.')
            longitude = extrair_meta_dados(linhas[5]).replace(',', '.')
            altitude = extrair_meta_dados(linhas[6]).replace(',', '.')

        
            # tem um erro que em algumas poucas planilhas (uns 0.5%) tem um "F" no lugar do valor da altitude
            try:
                altitude = float(altitude)
            except ValueError:
                altitude = VALOR_ALTURA_NULA


            # Lê o conteúdo do CSV (pula cabeçalhos)
            df = pd.read_csv(csvPath, encoding="ISO-8859-1", skiprows=8, sep=';', decimal=',', na_values=["-9999", "", " "])
            
            # remove a ultima coluna que foi criada sem querer por causa do ";" que usa pra separar as celualas
            df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

            # Renomeia todas as colunas do DF para nomes padroes pra futuras manipulaçoes e usa o index/a ordem dela
            # pq o nome varia entre elas mas o index nao 
            df.columns = COLUNAS_PADRAO

            # Converte primeira coluna para datetime
            df[DATA] = pd.to_datetime(df[DATA], format='mixed', dayfirst=False)
            df[HORA] = df[HORA].apply(extrair_hora)

            # trata os dados dos campos e validas eles, se estão dentro de limites aceitaveis
            df = validar_e_limpar_dados(df) 

            df = completar_datas_horas(df, ano)

            # validar o df antes de salvar 
            if not validar_df_nao_vazios(df, csvPath):
                continue

            # salvar o dados
            # Cria nome do arquivo parquet
            nome = f"{ano}_LA{int(float(latitude))}_LO{int(float(longitude))}_{codigo}.parquet"
            parquet_local_path = Path(PARQUET_LOCAL_DIR) / str(ano) / nome
            parquet_path = path.join(OUTPUT_DIR, str(ano), nome)

            df.to_parquet(parquet_path, index=False)

            registrosIndex.append({
                ARQUIVO: parquet_local_path.as_posix(),
                ANO: ano,
                REGIAO: regiao,
                UF: uf,
                ESTACAO: estacao,
                CODIGO: codigo,
                LATITUDE: float(latitude),
                LONGITUDE: float(longitude),
                ALTITUDE: float(altitude)
            })
        except Exception as e:
            print(f"[❌] Erro em {csvPath}: {e}")


    if registrosIndex:
        df_index_novo = pd.DataFrame(registrosIndex)
        df_index_novo.to_parquet(indexPath, index= False)
        print(f"[📁] Índice atualizado: {indexPath}")



def processar_csvs(arquivos_para_tratar : Queue, max_workers):
    with ProcessPoolExecutor(max_workers= max_workers) as executor:
        while True:
            arquivo = arquivos_para_tratar.get()
            if arquivo is None:
                break
            
            executor.submit(processar_csv, arquivo)