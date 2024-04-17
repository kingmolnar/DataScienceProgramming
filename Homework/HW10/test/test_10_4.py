import pandas as pd
import os

def test_10_4():
    assert os.path.isfile('model_10_4.json'), "Model has not been saved"
    assert os.path.isfile('output_10_4.csv'), "CSV file with test data and prediction is missing"
    df = pd.read_csv('output_10_4.csv')
    list(df.columns) == ['MedInc',  'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup',
                         'Latitude', 'Longitude', 'MedHouseVal', 'Predicted_MedHouseVal'], "Incomplete table"
