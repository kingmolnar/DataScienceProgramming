from solution_3_17 import get_consonants

def test_3_17():
    letters = ["a", "e", "i", "o", "u", "b", "c", "d", "f"]
    assert get_consonants(letters) == {'b', 'c', 'd', 'f'} , "Mismatch in the output"
