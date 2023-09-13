from solution_3_1 import calculate_tip

def test_3_1():
    assert calculate_tip(25,0.2) == 5.0, "Mismatch in output for test case 1"
    assert calculate_tip(33,0.3) == 9.9, "Mismatch in output for test case 2"
