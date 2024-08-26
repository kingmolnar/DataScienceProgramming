
import os
import re

def test_problem_1_13():
    pat = re.compile("|1$")
    filename = 'data/sentiment_positive.txt'
    assert os.path.isfile(filename), "Missing output file."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 1500, "Incorrect number of lines"
    for lin in lines:
        assert len(lin.split('|'))==1, "Invalid record format."
        assert lin == lin.lower()
