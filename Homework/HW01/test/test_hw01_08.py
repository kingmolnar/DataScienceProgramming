
import os
import re

def test_problem_1_8():
    filename = 'data/sentiment.tsv'
    assert os.path.isfile(filename), "Missing output file."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 3000, "Incorrect number of lines"
    for lin in lines:
        assert len(lin.split('\t'))==2, "Invalid record format."
    
