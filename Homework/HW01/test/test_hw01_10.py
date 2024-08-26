
import os
import re

def test_problem_1_10():
    filename = 'data/sentiment_lower.psv'
    assert os.path.isfile(filename), "Missing output file."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 3000, "Incorrect number of lines"
    for lin in lines:
        assert len(lin.split('|'))==2, "Invalid record format."
        assert lin == lin.lower()
