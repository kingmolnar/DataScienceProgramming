
import os
import re

def test_problem_1_6():
    assert os.path.isfile('output_1_6.txt'), "Missing output file."
    lines = open('output_1_6.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) == 20, "Incorrect number of lines"
