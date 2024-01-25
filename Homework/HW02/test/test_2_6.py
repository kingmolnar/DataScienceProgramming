from solution_2_6 import stat_measures

def test_2_6():
    file = '/data/kelleher/MotorInsuranceFraudClaim_ClaimAmountReceived.csv'
    res = stat_measures(file)
    assert int(res['mean']) == 13051, f'Incorrect value for mean'
    assert int(res['stddev']) == 30516, f'Incorrect value for stddev'
    assert int(res['min']) == 0, f'Incorrect value for min'
    assert int(res['max']) == 295303, f'Incorrect value for max'
    assert int(res['count']) == 500, f'Incorrect value for count'
