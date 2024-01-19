
import os
import re

def test_problem_1_9():
    filename = 'data/sentiment.psv'
    assert os.path.isfile(filename), "Missing output file."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 3000, "Incorrect number of lines"
    for lin in lines:
        assert len(lin.split('|'))==2, "Invalid record format."
  
