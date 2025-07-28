import pandas as pd
from app.core.const.clima import DATA



# converte o data frame para uma lista de lista
# if dataToStr converte para string a data em formato br
def converter_df_para_list(df : pd.DataFrame, dataToStr : bool = True) -> list:
    df_copy = df.copy()
    if dataToStr:
        df_copy[DATA] = df_copy[DATA].dt.strftime('%d-%m-%Y')

    resultado = [df_copy.columns.tolist()] + df_copy.values.tolist()
    return resultado



# converte o data frame para um obj parecido com json
def converter_df_para_objeto(df : pd.DataFrame) -> list:
    df_copy = df.copy()
    df_copy[DATA] = df_copy[DATA].dt.strftime('%d-%m-%Y')
    resultado = df_copy.to_dict(orient="records")
    return resultado