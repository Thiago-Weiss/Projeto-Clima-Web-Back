import pandas as pd
from app.core.const.clima import DATA
from app.core import RespostaFormato
import numpy as np





def converter_para_o_front(df : pd.DataFrame, formato : RespostaFormato) -> list:
    # converte a data para string
    if DATA in df.columns:
        df[DATA] = df[DATA].dt.strftime('%d-%m-%Y')

    # arredonda os valores quebrados
    df = df.round(3)

    # troca o NaN do pandas por None do Python
    df = df.replace({np.nan: None})

    match formato:
        case RespostaFormato.LISTA:
            return [df.columns.tolist()] + df.values.tolist()
 
        case RespostaFormato.OBJETO:
            return df.to_dict(orient="records")

        case RespostaFormato.LISTA_ALTERNATIVA:
            return {col: df[col].tolist() for col in df.columns}