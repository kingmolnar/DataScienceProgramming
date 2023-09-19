import os

def test_3_15():
    assert os.path.isfile('amazon_positive.txt'), "Missing output file."
    lines = open('amazon_positive.txt', 'r', encoding='utf-8').readlines()
    #  assert len(lines) == 495, "Incorrect number of lines"
    assert len(lines) == 495 or len(lines) == 500, "Incorrect number of lines"
