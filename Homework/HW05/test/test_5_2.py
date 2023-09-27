import numpy as np
from solution_5_2 import population_growth

def test_5_2():
    initial_population = 1000
    growth_rate = 0.05
    time_periods = [0, 1, 2, 3, 4, 5]
    
    result = population_growth(initial_population, growth_rate, time_periods)
    expected_result = initial_population * np.exp(growth_rate * np.array(time_periods))  
    
    assert np.allclose(result, expected_result), "The calculated populations are incorrect"
