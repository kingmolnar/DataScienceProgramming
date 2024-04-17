# from solution_10_2 import *
import pandas as pd
import numpy as np
import os

FILENAME = 'output_10_2.csv'
def test_10_2():
    assert os.path.isfile(FILENAME), f"File `{FILENAME}` does not exist"
    cmp_df2 = pd.read_csv(FILENAME)
    assert any(cmp_df2.columns.values == np.array(['feature', 'diff_mean', 'diff_std', 'diff_min', 'diff_25%',
           'diff_50%', 'diff_75%', 'diff_max'])), "Invalid columns"
    assert any(cmp_df2['feature'].values == np.array(['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population',
           'AveOccup', 'Latitude', 'Longitude', 'MedHouseVal'])), "Invalid features"
