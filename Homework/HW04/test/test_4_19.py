from solution_4_19 import find_growth_rate
import numpy as np

sales_data = np.array([
    ['Jan', 50000, 4500, 20000],
    ['Feb', 52000, 4600, 21000],
    ['Mar', 55000, 4800, 22000],
    ['Apr', 56000, 4900, 23000],
    ['May', 58000, 5100, 24000]
])

def test_4_19():
    assert find_growth_rate(sales_data) == [4.16, 5.41, 2.57, 3.81], "Incorrect output"
