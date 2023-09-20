import os
import pandas as pd
import solution_4_22

def test_4_22():
    assert 'df' in dir(solution_4_22), "`df` is not defined"
    df = solution_4_22.df
    assert str(type(df)) == "<class 'pandas.core.frame.DataFrame'>", "Incorrect type df"
    assert str(df.columns) == "Index(['Name', 'Age', 'City'], dtype='object')", "Incorrect columns"
    assert str(len(df['Name'])) == "3", "Incorrect number of Name"
    assert str(len(df['Age'])) == "3", "Incorrect number of Age "
    assert str(len(df['City'])) == "3", "Incorrect number of City"
