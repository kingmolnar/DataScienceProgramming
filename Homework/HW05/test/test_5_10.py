from solution_5_10 import find_drama_movies_1994_below_9_rating

def test_5_10():
    result = find_drama_movies_1994_below_9_rating()
    expected_result = ['Forrest Gump']
    assert result == expected_result, 'The output provided is incorrect'
