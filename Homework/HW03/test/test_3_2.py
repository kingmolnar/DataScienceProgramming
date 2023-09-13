from solution_3_2 import calculate_shipping_cost

def test_3_2():
    assert calculate_shipping_cost(10,250) == 32.50, "Mismatch in output for test case 1"
    assert calculate_shipping_cost(14, 325) == 41.25, "Mismatch in output for test case 2"
