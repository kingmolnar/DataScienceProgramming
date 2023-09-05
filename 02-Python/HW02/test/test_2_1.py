import os

def test_2_1():
    lines = open('output_2_1.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) == 20, "Incorrect number of lines in output."
