
import os
import re

def test_problem_1_21():
    
    pat = re.compile(r'(\w+)\s(\d+)\s(\d+)')
                     
    def is_sorted(lines):
        freq_list = [ s.strip().split(' ')[1].strip() for s in lines ]
        freq_sort = sorted(freq_list, reverse=False)
        return all([ t[0] == t[1] for t in zip(freq_list, freq_sort) ])
    
    filenames = [
        'data/joined_words.lst',
    ]
    for fn in filenames:
        assert os.path.isfile(fn), f"File does not exist: {fn}"
        lines = open(fn, 'r', encoding='utf-8').readlines()
        lines2 = list(filter(lambda s: pat.match(s), lines))
        assert len(lines) == len(lines2), f"Not all records match format {len(lines)}/{len(lines2)}"
        
    
    
