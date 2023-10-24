#from solution_6_2 import *
import pandas as pd

def test_6_2():
    df = pd.read_csv('athlete_events_6_2.csv')
    assert df.Medal.isnull().sum() == 0, 'There are still missing values in that column'
