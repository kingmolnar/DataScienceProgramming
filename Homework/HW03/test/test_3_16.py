from solution_3_16 import get_countries_with_capital_starting_with_p

def test_3_16():
    dict1 = {"China": "Beijing", "France": "Paris", "India": "New Delhi", "Poland": "Warsaw"}
    assert get_countries_with_capital_starting_with_p(dict1) == ['France'], "Incorrect output"
