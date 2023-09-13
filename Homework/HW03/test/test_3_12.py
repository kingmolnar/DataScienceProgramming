from solution_3_12 import generate_even_numbers

def test_3_12():
    assert list(generate_even_numbers(21, skip_divisible_by_4=False)) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20], "generate_even_numbers is not correct"
