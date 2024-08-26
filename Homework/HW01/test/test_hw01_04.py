
import os
import re

def test_problem_1_4():
    pat = "/data/IFI8410/sess01/sentiment_labelled_sentences/"
    assert os.path.isfile('output_1_4.txt'), "Missing output file."
    lines = open('output_1_4.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) == 3, "Incorrect number of lines"
    for lin in lines:
        assert pat in lin, f"Invalid content: {lin}"
  
