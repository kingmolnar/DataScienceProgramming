import os
def test_8_2():
    filename = 'answer_8_2.txt'
    assert os.path.isfile(filename), f"Missing file `{filename}`"
    lines = filter(
        lambda s: not s.startswith('#'),
        map(
            lambda s: s.strip(),
            open(filename, "r", encoding='utf-8').readlines()
        )
    )
    text = '\n'.join(lines)
    assert len(text)>0, f"No contents in answer file `{filename}`"
