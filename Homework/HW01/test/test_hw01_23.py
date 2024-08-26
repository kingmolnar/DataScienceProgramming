
import os
import re

def test_problem_1_23():
    
    pat = re.compile(r'(\w+)')
                     
    def is_sorted(lines):
        freq_list = [ s.strip().split(' ')[1].strip() for s in lines ]
        freq_sort = sorted(freq_list, reverse=False)
        return all([ t[0] == t[1] for t in zip(freq_list, freq_sort) ])
    
    filenames = [
        'data/top_100_positive_words.lst',
        'data/top_100_negative_words.lst',
    ]
    for fn in filenames:
        assert os.path.isfile(fn), f"File does not exist: {fn}"
        lines = open(fn, 'r', encoding='utf-8').readlines()
        lines1 = list(filter(lambda s: len(s)>0, lines))
        assert len(lines1)==100, f"Invalid number of lines: {len(lines1)}"
        lines2 = list(filter(lambda s: pat.match(s), lines1))
        assert len(lines1) == len(lines2), f"Not all records match format {len(lines)}/{len(lines2)}"
        
