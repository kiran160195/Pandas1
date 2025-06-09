import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    condition = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    df = condition[['name','population','area']]

    return df

