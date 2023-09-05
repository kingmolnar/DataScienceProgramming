from datetime import datetime
from solution_2_12 import delta_minutes

def test_2_12():
    t1 = datetime(2003, 3, 14, 0, 1, 3)
    t2 = datetime(2014, 3, 14, 0, 1, 3)
    minutes = delta_minutes(t2, t1)
    assert int(minutes)==5785920, "Invalid result"
