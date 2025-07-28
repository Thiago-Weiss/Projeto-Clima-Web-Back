import pandas as pd
from app.core.const.clima import DATA


# filtra pelo perido de tempo
def filtrar_por_datas(df : pd.DataFrame, dt_inicio : pd.Timestamp, dt_fim : pd.Timestamp) -> pd.DataFrame:
    df[DATA] = pd.to_datetime(df[DATA])        
    df = df[(df[DATA] >= dt_inicio) & (df[DATA] <= dt_fim)]
    df = df.sort_values(DATA).reset_index(drop=True)
    return df

