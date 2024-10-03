import pandas as pd


def get_and_clean(type: str) -> pd.DataFrame | str:
    """
    This is a simple function responsible to get .csv files based in their type.
    Args:
        type (str): The first parameter, representing a string. It can be 'raw' or 'gold'.
    Returns:
       Pandas DataFrame: A DataFrame containing the raw or gold data from the .csv file.
    Raises:
        ValueError: If `param2` is not a positive integer.
    """

    if (type == 'raw'):
        df = pd.read_csv('../../dataset/raw/dataset.csv')
        df.columns = [col.lower().replace(' ', '_') for col in df.columns]
        return df

    elif (type == 'gold'):
        df = pd.read_csv('../../dataset/gold/dataset.csv')
        df.columns = [col.lower().replace(' ', '_') for col in df.columns]
        return df
    else:
        return "Invalid dataset type"
