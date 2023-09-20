from solution_4_4 import solar_power_calculator

def test_4_4():
    assert round(solar_power_calculator( 20, 0.18, 1000),2) == 21.6, "Output is incorrect for testcase 1"
    assert round(solar_power_calculator(66, 0.25, 1200),2) == 118.8, "Output is incorrect for testcase 2"
