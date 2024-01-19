
import os
import re

def test_problem_1_20():
    def is_sorted(lines):
        freq_list = [ s.strip().split(' ')[1].strip() for s in lines ]
        freq_sort = sorted(freq_list, reverse=False)
        return all([ t[0] == t[1] for t in zip(freq_list, freq_sort) ])
    
    filenames = [
        'data/positive_words_alphabetic_order.lst',
        'data/negative_words_alphabetic_order.lst'
    ]
    for fn in filenames:
        assert os.path.isfile(fn), f"File does not exist: {fn}"
        lines = open(fn, 'r', encoding='utf-8').readlines()
        lines2 = list(filter(lambda s: len(s)>1, lines))
        assert is_sorted(lines2), "List is not sorted."
        
    
    
