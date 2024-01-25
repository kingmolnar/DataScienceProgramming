from solution_2_5 import text_translate

from tempfile import NamedTemporaryFile
import os
import re
pat = re.compile(r'[A-Z]')


def test_2_5():
    translation = {
        'beloved': 'geliebter',
        'loves': 'liebt',
        'loved': 'geliebt',
        'love': 'liebe',
    }
    f = NamedTemporaryFile(delete=False)
    fn = f.name
    f.close()
    in_file = '/data/pg100_lower_case.txt'
    text_translate(in_file, fn, translation)
    assert os.path.exists(fn), "Failed to create file"
    text = open(fn, 'r', encoding='utf-8').readlines()
    N_love = len([line for line in text if 'love' in line])
    N_liebe = len([line for line in text if 'liebe' in line])
    
    assert N_love == 0, f"Found {N_love} instances of 'love', should be 0"
    assert N_liebe == 2363, f"Found {N_liebe} instances of 'love', should be 2363"
    os.unlink(fn)
    assert not os.path.exists(fn), f"File `{fn}` should have been deleted"
