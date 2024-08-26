
import os
import re

def test_problem_1_17():
    word_list = ['990 the', '669 and', '466 a', '418 i', '417 is', '326 this',
                  '311 it', '308 of', '305 to', '257 was', '205 in', '198 great',
                  '176 good', '159 for', '157 with', '146 very', '126 that', '125 my',
                  '108 on', '102 are']
    filename = "output_1_17.txt"
    assert os.path.isfile(filename), f"Missing output file: {filename}."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 20, "Incorrect number of lines"
    #     pairs = zip(word_list, map(str.strip, lines))
    #     for p in pairs:
    #         assert p[0] == p[1], f"Mismatch: `{p[0]}` vs `{p[1]}`"
        
