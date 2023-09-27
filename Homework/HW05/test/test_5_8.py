from solution_5_8 import find_least_rated_movie

def test_5_8():
    result = find_least_rated_movie()    
    assert result == ('Titanic', 7.8), 'The output provided is incorrect'
