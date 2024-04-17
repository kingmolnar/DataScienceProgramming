
from solution_10_1 import split_dataframe
import pandas as pd


def test_10_1():
    df = pd.read_csv('/data/IFI8410/california_housing/california_housing.csv', nrows=100)
    df1, df2 = split_dataframe(df, 0.5)
    assert round(df1.shape[0]/10) == round(df2.shape[0]/10), "Invalid split"
    assert df1.shape[0] +  df2.shape[0] == df.shape[0], "Incorrect number of records"
    assert df1.shape[1] == df.shape[1], "Column mismatch"
    assert df2.shape[1] == df.shape[1], "Column mismatch"
