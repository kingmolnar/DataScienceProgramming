import os
import solution_4_15
import numpy as np

def test_4_15():
    assert 'historical_sales' in dir(solution_4_15), "`historical_sales` is not defined"
    historical_sales = solution_4_15.historical_sales

    assert 'growth_factors' in dir(solution_4_15), "`growth_factors` is not defined"
    growth_factors = solution_4_15.growth_factors

    assert 'projected_sales' in dir(solution_4_15), "`projected_sales` is not defined"
    projected_sales = solution_4_15.projected_sales


    expected_historical_sales = np.array([250, 280, 300, 320, 350, 380, 400, 420, 450, 480, 500, 520])

    expected_growth_factors = np.array([1.05, 1.08, 1.12])

    expected_projected_sales = np.dot(historical_sales[-3:], growth_factors)

    assert str(type(historical_sales)) == "<class \'numpy.ndarray\'>", "Incorrect type historical_sales"
    assert str(type(growth_factors)) == "<class \'numpy.ndarray\'>", "Incorrect type growth_factors"
    assert str(type(projected_sales)) == "<class \'numpy.float64\'>", "Incorrect type projected_sales"

    assert np.allclose(historical_sales, expected_historical_sales), "Incorrect historical_sales"
    assert np.allclose(growth_factors, expected_growth_factors), "Incorrect growth_factors"
    assert np.allclose(projected_sales, expected_projected_sales), "Incorrect projected_sales"
