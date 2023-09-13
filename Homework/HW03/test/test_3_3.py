from solution_3_3 import calculate_age
import datetime

def test_3_3():
    assert round(calculate_age(datetime.date(2005, 7, 15)), 2) == 18.14, "Output is incorrect"
