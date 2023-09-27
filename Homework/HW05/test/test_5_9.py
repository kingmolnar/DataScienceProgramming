from solution_5_9 import count_movie_genres

def test_5_8():
    result = count_movie_genres()
    expected_result = {
        'Sci-Fi': 3,
        'Crime': 2,
        'Drama': 3,
        'Action': 1,
        'Romance': 1
    }
    
    assert result == expected_result, 'The output provided is incorrect'
