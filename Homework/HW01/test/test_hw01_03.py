
import os
import re

def test_problem_1_3():
    pat = re.compile(r"/data/IFI8410/sess01")
    assert os.path.isfile('output_1_3.txt'), "Missing output file."
    lines = open('output_1_3.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) > 0, "Empty file."
    assert len(list(filter(pat.match, lines))) > 0, "Missing content"
  
