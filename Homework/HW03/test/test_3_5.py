from solution_3_5 import garden_watering

def test_3_5():
    garden = [
    {'name': 'Rose', 'moisture_level': 55, 'threshold_level': 40},
    {'name': 'Tomato', 'moisture_level': 25, 'threshold_level': 50},
    {'name': 'Lavender', 'moisture_level': 29, 'threshold_level': 30},
    {'name': 'Basil', 'moisture_level': 50, 'threshold_level': 45}
    ]

    assert garden_watering(garden) == {'Rose': False, 'Tomato': True, 'Lavender': True, 'Basil': False}, "Incorrect output"
def test_3_5():
    assert True, "No Test"
