
from solution_2_1 import calculate_averages

from numpy.testing import assert_approx_equal

def test_hw02_01():
    student_scores = {
    "Alice": [85, 90, 78],
    "Bob": [70, 88, 92],
    "Charlie": [80, 85, 85],
    "David": [95, 100, 98]
    }
    results = calculate_averages(student_scores)
    assert_approx_equal(results['Alice'], 84.333, significant=5)
    assert_approx_equal(results['David'], 97.666, significant=5)
