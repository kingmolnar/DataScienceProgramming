from solution_2_3 import linecount

def test_2_3():
    fnln = [ ('/data/IFI8410/sess01/legalnotice.txt', 291),
             ('/data/IFI8410/sess01/sentiment_labelled_sentences/readme.txt', 31),
             ('/data/IFI8410/churn_data.csv', 7043) ]
    for fn, ln in fnln:
        cn = linecount(fn)
        assert cn == ln, f"Incorrect count of lines for file {fn}: {cn:,} should be {ln:,}"
