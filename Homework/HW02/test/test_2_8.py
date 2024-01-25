from solution_2_8 import calc_claims
import numpy as np

def test_2_8():
    data_file = '/data/kelleher/MotorInsuranceFraudClaim_Claimed_vs_Received.csv'
    perc_diff = calc_claims(data_file)

    assert perc_diff.shape[0] == 331, "Invalid number of rows. Did you filter for completed claims?"
    hist = np.histogram(perc_diff, 10)

    freq = hist[0]
    bounds = hist[1]
    assert int(bounds[0]) == -22, f'Invalid bound' 
    assert int(bounds[1]) == -19, f'Invalid bound' 
    assert int(bounds[2]) == -17, f'Invalid bound' 
    assert int(bounds[3]) == -15, f'Invalid bound' 
    # assert int(bounds[4]) == -12, f'Invalid bound' 
    assert int(bounds[5]) == -10, f'Invalid bound' 
    assert int(bounds[6]) == -8, f'Invalid bound' 
    assert int(bounds[7]) == -6, f'Invalid bound' 
    assert int(bounds[8]) == -4, f'Invalid bound' 
    assert int(bounds[9]) == -1, f'Invalid bound' 
    assert int(bounds[10]) == 0, f'Invalid bound' 
    assert freq[0] ==  1, f'Invalid frequency' 
    assert freq[1] ==  0, f'Invalid frequency' 
    assert freq[2] ==  0, f'Invalid frequency' 
    assert freq[3] ==  0, f'Invalid frequency' 
    assert freq[4] ==  0, f'Invalid frequency' 
    assert freq[5] ==  0, f'Invalid frequency' 
    assert freq[6] ==  0, f'Invalid frequency' 
    assert freq[7] ==  3, f'Invalid frequency' 
    assert freq[8] ==  7, f'Invalid frequency' 
    assert freq[9] ==  320, f'Invalid frequency'
    
