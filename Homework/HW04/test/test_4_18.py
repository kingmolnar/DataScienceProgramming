from solution_4_18 import find_best_month
import numpy as np

sales_data = np.array([
    ['Jan', 50000, 4500, 20000],
    ['Feb', 52000, 4600, 21000],
    ['Mar', 55000, 4800, 22000],
    ['Apr', 56000, 4900, 23000],
    ['May', 58000, 5100, 24000]
])

def test_4_18():
    best_month, best_month_revenue = find_best_month(sales_data)
    assert best_month == 'May', "The best month found is incorrect"
    assert str(best_month_revenue) == '87100', "The best month revenue found is incorrect"
