
import os
import re

def test_problem_1_5():
    assert os.path.isfile('output_1_5.txt'), "Missing output file."
    lines = open('output_1_5.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) == 20, "Incorrect number of lines"
