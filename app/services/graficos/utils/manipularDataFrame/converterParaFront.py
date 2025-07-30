import pandas as pd
from app.core.const.clima import DATA
from app.core import RespostaFormato


# converte o data frame para uma lista de lista
def converter_df_para_list(df : pd.DataFrame) -> list:
    df_copy = df.copy()
    df_copy[DATA] = df_copy[DATA].dt.strftime('%d-%m-%Y')
    resultado = [df_copy.columns.tolist()] + df_copy.values.tolist()
    return resultado



# converte o data frame para um obj parecido com json
def converter_df_para_objeto(df : pd.DataFrame) -> list:
    df_copy = df.copy()
    df_copy[DATA] = df_copy[DATA].dt.strftime('%d-%m-%Y')
    resultado = df_copy.to_dict(orient="records")
    return resultado


def converter_df_para_lista_alternativa(df : pd.DataFrame) -> list:
    df_copy = df.copy()
    df_copy[DATA] = df_copy[DATA].dt.strftime('%d-%m-%Y')
    return{col: df_copy[col].tolist() for col in df_copy.columns}


def converter_para_o_front(df : pd.DataFrame, formato : RespostaFormato) -> list:
    match formato:
        case RespostaFormato.LISTA:
            return converter_df_para_list(df)
        
        case RespostaFormato.OBJETO:
            return converter_df_para_objeto(df)
    
        case RespostaFormato.LISTA_ALTERNATIVA:
            return converter_df_para_lista_alternativa(df)