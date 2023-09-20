import os
import pandas as pd
import solution_4_23
import numpy as np


def test_4_23():
    assert 'df' in dir(solution_4_23), "`df` is not defined"
    df = solution_4_23.df
    assert str(type(df)) == "<class 'pandas.core.frame.DataFrame'>", "Incorrect type df"

    assert 'filtered_df' in dir(solution_4_23), "`filtered_df` is not defined"
    filtered_df = solution_4_23.filtered_df
    assert str(type(filtered_df)) == "<class 'pandas.core.frame.DataFrame'>", "Incorrect type filtered_df"

    assert str(df.columns) == "Index(['Name', 'Age', 'City'], dtype='object')", "Incorrect columns"
    assert str(len(df['Name'])) == "3", "Incorrect number of Name"
    assert str(len(df['Age'])) == "3", "Incorrect number of Age "
    assert str(len(df['City'])) == "3", "Incorrect number of City"

    filtered_df_values = str(filtered_df.values)
    filtered_df_computed = df[df['Age'] >= 30]
    filtered_df_computed_values = str(filtered_df_computed.values)

    assert filtered_df_values == filtered_df_computed_values, "filtered_df is incorrect"
