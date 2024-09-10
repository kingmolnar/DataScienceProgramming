
from solution_2_2 import aggregate

from numpy.testing import assert_equal

def test_hw02_02():
    averages = {
        "Alice": 84.33,
        "Bob": 83.33,
        "Charlie": 83.33,
        "David": 97.67
    }
    result = aggregate(averages)
    assert_equal(result, 87.165)
