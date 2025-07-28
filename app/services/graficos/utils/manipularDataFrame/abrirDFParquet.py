import pandas as pd
from os import path


def abrir_data_frame(arquivo, colunas) -> None | pd.DataFrame :
    # verifica se o arquivo existe
    if not path.exists(arquivo):
        return None

    # retorna o data frame
    return pd.read_parquet(arquivo, columns= colunas)