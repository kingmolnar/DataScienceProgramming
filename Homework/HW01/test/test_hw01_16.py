
import os
import re

def test_problem_1_16():
    pat = re.compile(r"^[\w]+")
    filenames = [
        'data/sentiment_positive_words.txt',
        'data/sentiment_negative_words.txt'
    ]
    for fn in filenames:
        assert os.path.isfile(fn), f"Missing output file: {fn}."
        lines = open(fn, 'r', encoding='utf-8').readlines()
        for lin in lines:
            llin = lin.strip()
            assert len(llin)==0 or pat.match(llin), f"Invalid character: `{llin}`."
            
