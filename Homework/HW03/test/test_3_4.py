from solution_3_4 import calculate_quotient_and_remainder

def test_3_4():
    assert calculate_quotient_and_remainder(10, 3) == (3, 1), "Mismatch in output for test case 1"
    assert calculate_quotient_and_remainder(15, 4) == (3, 3), "Mismatch in output for test case 2"
