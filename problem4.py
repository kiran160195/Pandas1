import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    condition = customers[~customers['id'].isin(orders['customerId'])]
    return condition[['name']].rename(columns={'name': 'Customers'})
