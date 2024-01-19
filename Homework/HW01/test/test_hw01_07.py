
import os
import re

def test_problem_1_7():
    pat = re.compile(r"\s+(\d+)\s(\d+)\s(\d+)\s/data/IFI8410/sess01/sentiment_labelled_sentences/")
    assert os.path.isfile('output_1_7.txt'), "Missing output file."
    lines = open('output_1_7.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) == 3, "Incorrect number of lines"
    for lin in lines:
        m = pat.match(lin)
        assert m, f"Invalid content: {lin}"
        assert int(m.group(1)) == 1000, "Wrong number of records."
