import os
def test_2_2():
    assert int(os.popen("wc -l newsgroup_senders.txt").read().strip().split(' ')[0]) > 20_000, \
        "Not enought records."
