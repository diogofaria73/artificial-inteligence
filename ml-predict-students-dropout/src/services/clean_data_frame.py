import pandas as pd


def remove_empty_rows(df: pd.DataFrame) -> pd.DataFrame:

    if (df.isna().sum().all() > 0):
        return df.dropna()
    else:
        return df
