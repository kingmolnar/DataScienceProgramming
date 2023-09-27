import numpy as np
from solution_5_4 import currency_exchange_2

def test_5_4():
    exchange_rate_matrix = np.array([[1.0, 1/0.94, 1/147.83],      
                                     [0.94, 1.0, 1/157.62], 
                                     [147.83, 157.62, 1.0]] )
    
    source_amount = np.array([100.0, 0.0, 0.0])
    result = currency_exchange_2(exchange_rate_matrix, source_amount,'EUR')
    
    assert result == 94., "The conversion is incorrect"
