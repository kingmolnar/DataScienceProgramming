from solution_2_23 import flat_list

def test_2_23():
    nested_list = [["John"], ["Emily", "Maria", "Juan", "Javier"]]
    result = ['John', 'Emily', 'Maria', 'Juan', 'Javier']
    assert result == flat_list(nested_list), "Incorrect result"
