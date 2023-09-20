import os
import pandas as pd
import solution_4_25
import numpy as np


def test_4_25():
    assert 'df' in dir(solution_4_25), "`df` is not defined"
    df = solution_4_25.df
    assert str(type(df)) == "<class 'pandas.core.frame.DataFrame'>", "Incorrect type df"

    assert 'sorted_df' in dir(solution_4_25), "`sorted_df` is not defined"
    sorted_df = solution_4_25.sorted_df
    assert str(type(sorted_df)) == "<class 'pandas.core.frame.DataFrame'>", "Incorrect type sorted_df"

    assert str(df.columns) == "Index(['Name', 'Age', 'City'], dtype='object')", "Incorrect columns"
    assert str(len(df['Name'])) == "3", "Incorrect number of Name"
    assert str(len(df['Age'])) == "3", "Incorrect number of Age "
    assert str(len(df['City'])) == "3", "Incorrect number of City"


    sorted_df_values = str(sorted_df.values)
    sorted_df_computed = df.sort_values(by='Age', ascending=False)
    sorted_df_computed_values = str(sorted_df_computed.values)

    assert sorted_df_values == sorted_df_computed_values, "sorted_df is incorrect"
