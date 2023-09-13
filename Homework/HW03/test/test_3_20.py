import os

def test_3_19():
    assert os.path.isfile('output_yelp.txt'), "Missing output file."
    lines = open('output_yelp.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) == 50, "Incorrect number of lines"
    assert lines[0].strip().startswith('Wow... Loved this place.')
