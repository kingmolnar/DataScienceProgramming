from solution_3_13 import safe_divide


def test_3_13():
    assert safe_divide(5, 0) == "Division by zero is not allowed.", "safe_divide is not correct"
    assert safe_divide(0, 5) == 0.0, "safe_divide is not correct"

