from solution_6_1 import *

def test_6_1():
    data = '/data/kelleher/MotorInsuranceFraudClaim_clean.csv'
    df = pd.read_csv(data)
    df_train, df_test = split_data_set(df, 0.5)
    assert df.shape[1]==df_train.shape[1], "Mismatching columns in first dataframe"
    assert df.shape[1]==df_test.shape[1], "Mismatching columns in second dataframe"
    assert df_train.shape[0]==df_test.shape[0], "Split dataframes should have same number of rows"
    assert df.shape[0]==(df_train.shape[0]+df_test.shape[0]), "Number or rows doesn't add up"
