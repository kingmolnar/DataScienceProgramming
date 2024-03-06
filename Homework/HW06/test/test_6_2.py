import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from solution_6_2 import *

def test_6_2():
    df = pd.read_csv('/data/kelleher/MotorInsuranceFraudClaim_clean.csv')
    categorical_features = ['InsuranceType', 'MaritalStatus', 'OvernightHospitalStay', 'InjuryType']
    my_encoder = create_one_hot_encoder(df, categorical_features)
    assert isinstance(my_encoder, OneHotEncoder), "Invalid type"
    assert len(my_encoder.categories_)==4, "Invalid number of categories"
