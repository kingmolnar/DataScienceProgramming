from solution_3_2 import get_total_grocery_bill

products = [
    {"name": "Apple", "price": 1.50},
    {"name": "Banana", "price": 0.50},
    {"name": "Orange", "price": 2.00},
    {"name": "Milk", "price": 3.00},
]
quantities= [
    {"name": "Apple", "quantit": 3},
    {"name": "Banana", "quantit": 6},
    {"name": "Orange", "quantit": 2.00},
    {"name": "Milk", "quantit": 3.00},
]

def test_3_2():
    assert get_total_grocery_bill(products, quantities) == 20.5,  "Incorrect output"
