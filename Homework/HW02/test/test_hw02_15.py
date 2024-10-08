
from solution_2_15 import convert_to_lower_case

import os
import re
pat = re.compile(r'[A-Z]')

def test_2_15():
    fn = 'lower_case_text_imported.txt'
    infile = '/data/pg100.txt'
    convert_to_lower_case(infile, fn)
    assert os.path.exists(fn), "Failed to create file"
    text = open(fn, 'r', encoding='utf-8').read()
    assert pat.search(text) == None, "Found upper case letters in text"
    os.unlink(fn)
    assert not os.path.exists(fn), f"File `{fn}` should have been deleted"
