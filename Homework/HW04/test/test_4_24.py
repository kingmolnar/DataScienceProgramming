import os
import pandas as pd
import solution_4_24
import numpy as np


def test_4_24():
    assert 'df' in dir(solution_4_24), "`df` is not defined"
    df = solution_4_24.df
    assert str(type(df)) == "<class 'pandas.core.frame.DataFrame'>", "Incorrect type df"

    assert 'average_age' in dir(solution_4_24), "`average_age` is not defined"
    average_age = solution_4_24.average_age
    assert str(type(average_age)) == "<class 'numpy.float64'>", "Incorrect type average_age"

    assert str(df.columns) == "Index(['Name', 'Age', 'City'], dtype='object')", "Incorrect columns"
    assert str(len(df['Name'])) == "3", "Incorrect number of Name"
    assert str(len(df['Age'])) == "3", "Incorrect number of Age "
    assert str(len(df['City'])) == "3", "Incorrect number of City"

    average_age_computed = df['Age'].mean()

    assert np.allclose(average_age, average_age_computed), "average_age is incorrect"
