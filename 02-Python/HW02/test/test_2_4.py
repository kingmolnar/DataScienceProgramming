import os
def test_2_4():   
    assert os.path.isfile('newsgroup_raw_table.csv'), "File does not exist"
    lines = open('newsgroup_raw_table.csv', 'r', errors='ignore').readlines()
    assert len(lines)> 20_000, "Not enought records"
    assert not any(list(filter(lambda s: ':' in s or '/' in s, lines))), "Some lines contain `/` or ':'"
    assert len(list(filter(lambda s: len(s.split(','))==3, lines))) == len(lines), "Incorrect number of columns"
