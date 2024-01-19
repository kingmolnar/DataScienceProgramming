
import os
import re

def test_problem_1_15():
    filenames = [
        'data/sentiment_positive_tokens.txt',
        'data/sentiment_negative_tokens.txt'
    ]
    for fn in filenames:
        assert os.path.isfile(fn), f"Missing output file: {fn}."
        lines = open(fn, 'r', encoding='utf-8').readlines()
        for lin in lines:
            assert ' ' not in lin.strip(), "Invalid character."
        
