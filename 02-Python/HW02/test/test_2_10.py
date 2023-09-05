from solution_2_10 import is_positive

def test_2_10():
    for x in [74, -5.9, 10.2, -99.9, 82.7, -0.4]:
        assert (x>0) == is_positive(x), f"Invalid result for {x}"
