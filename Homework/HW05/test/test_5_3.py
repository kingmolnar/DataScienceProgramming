import numpy as np
from solution_5_3 import currency_exchange

def test_5_3():
    exchange_rate_matrix = np.array([[1.0, 1/0.94, 1/147.83],      
                                     [0.94, 1.0, 1/157.62], 
                                     [147.83, 157.62, 1.0]] )
    
    source_amount = np.array([100.0, 0.0, 0.0])
    result = currency_exchange(exchange_rate_matrix, source_amount)
    expected_result = np.array([100.0, 94.0, 14783.0])
    assert np.allclose(result, expected_result), "The conversion is incorrect"
