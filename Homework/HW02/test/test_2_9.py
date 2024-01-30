from solution_2_9 import load_data_col
import numpy as np

def test_2_9():
    # claimed_file = 'MotorInsuranceFraud_ClaimAmount.csv'
    claimed_file = '/data/kelleher/MotorInsuranceFraudClaim_ClaimAmount.csv'    
    x = load_data_col(claimed_file)
    if isinstance (x, np.ndarray):
        assert x.shape == (500,), "Invalid number of records"
        assert type(x[0]) == np.float64, "Invalid data type"
    else:
        assert isinstance(x, list), "This is not a list"
        assert all([isinstance(v, float) for v in x]), "All elements must be of type float"
