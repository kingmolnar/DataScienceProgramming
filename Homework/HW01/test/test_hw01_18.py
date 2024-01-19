
import os
import re

def test_problem_1_18():
    word_list = ['951 the', '469 i', '460 and', '420 a', '361 to', '354 it',
                 '336 is', '314 of', '313 this', '312 was', '250 not', '193 in',
                 '177 that', '177 for', '126 my', '116 with', '114 but',
                 '111 you', '111 on', '97 very']
    filename = "output_1_18.txt"
    assert os.path.isfile(filename), f"Missing output file: {filename}."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 20, "Incorrect number of lines"
    #     pairs = zip(word_list, map(str.strip, lines))
    #     for p in pairs:
    #         assert p[0] == p[1], f"Mismatch: `{p[0]}` vs `{p[1]}`"
        
   
