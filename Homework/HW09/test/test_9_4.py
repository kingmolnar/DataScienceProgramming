from solution_9_4 import (
    vectorize_product,
    aggregate_customer_products
)
import pandas as pd
import numpy as np

def test_9_4():
    df1 = pd.read_csv('/data/IFI8410/online_retail/customer_product_transactions.csv', nrows=200)
    df2 = vectorize_product(df1)
    df3 = aggregate_customer_products(df2)
    assert df2.shape[0] == df1.shape[0], 'Problem with length of data frame'
    assert df2.shape[1] == 3, 'Invalid number of columns'
    assert isinstance(df2.iloc[0].StockCodeVec, np.ndarray), 'Incorrect data type of vector column'
    assert df3.shape == (151, 2), 'Incorrect shape of profile table'
    assert isinstance(df3.iloc[0].StockCodeVec, np.ndarray), 'Incorrect data type of vector column'
