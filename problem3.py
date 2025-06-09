import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    '''Simple pandas & condition'''
    condition = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]

    product_ids = condition[['product_id']]

    return product_ids