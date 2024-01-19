
import os
import re

def test_problem_1_2():
    pat = re.compile(r"^\.\w+")
    assert os.path.isfile('output_1_2.txt'), "Missing output file."
    lines = open('output_1_2.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) > 0, "Empty file."
    assert len(list(filter(pat.match, lines))) > 0, "No hidden files."
                          
