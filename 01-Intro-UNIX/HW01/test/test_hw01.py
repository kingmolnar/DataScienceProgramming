#!/bin/bash


# ██╗  ██╗ ██████╗ ███╗   ███╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗     ██╗
# ██║  ██║██╔═══██╗████╗ ████║██╔════╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝    ███║
# ███████║██║   ██║██╔████╔██║█████╗  ██║ █╗ ██║██║   ██║██████╔╝█████╔╝     ╚██║
# ██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  ██║███╗██║██║   ██║██╔══██╗██╔═██╗      ██║
# ██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗     ██║
# ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝
   

import os
import re

def test_problem_1_1():
    assert os.path.isdir('data'), "The directory `data` does not exist."
    

def test_problem_1_2():
    pat = re.compile(r"^\.\w+")
    assert os.path.isfile('output_1_2.txt'), "Missing output file."
    lines = open('output_1_2.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) > 0, "Empty file."
    assert len(list(filter(lambda x: pat.match(x), lines))) > 0, "No hidden files."
                          

def test_problem_1_3():
    pat = re.compile(r"/data/IFI8410/sess01")
    assert os.path.isfile('output_1_3.txt'), "Missing output file."
    lines = open('output_1_3.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) > 0, "Empty file."
    assert len(list(filter(lambda x: pat.match(x), lines))) > 0, "Missing content"
    

def test_problem_1_4():
    pat = "/data/IFI8410/sess01/sentiment_labelled_sentences/"
    assert os.path.isfile('output_1_4.txt'), "Missing output file."
    lines = open('output_1_4.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) == 3, "Incorrect number of lines"
    for lin in lines:
        assert pat in lin, f"Invalid content: {lin}"
        

def test_problem_1_5():
    assert os.path.isfile('output_1_5.txt'), "Missing output file."
    lines = open('output_1_5.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) == 20, "Incorrect number of lines"

    
def test_problem_1_6():
    assert os.path.isfile('output_1_6.txt'), "Missing output file."
    lines = open('output_1_6.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) == 20, "Incorrect number of lines"

    
def test_problem_1_7():
    pat = re.compile(r"\s+(\d+)\s(\d+)\s(\d+)\s/data/IFI8410/sess01/sentiment_labelled_sentences/")
    assert os.path.isfile('output_1_7.txt'), "Missing output file."
    lines = open('output_1_7.txt', 'r', encoding='utf-8').readlines()
    assert len(lines) == 3, "Incorrect number of lines"
    for lin in lines:
        m = pat.match(lin)
        assert m, f"Invalid content: {lin}"
        assert int(m.group(1)) == 1000, "Wrong number of records."


def test_problem_1_8():
    filename = 'data/sentiment.tsv'
    assert os.path.isfile(filename), "Missing output file."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 3000, "Incorrect number of lines"
    for lin in lines:
        assert len(lin.split('\t'))==2, "Invalid record format."
    

def test_problem_1_9():
    filename = 'data/sentiment.psv'
    assert os.path.isfile(filename), "Missing output file."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 3000, "Incorrect number of lines"
    for lin in lines:
        assert len(lin.split('|'))==2, "Invalid record format."
        

def test_problem_1_10():
    filename = 'data/sentiment_lower.psv'
    assert os.path.isfile(filename), "Missing output file."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 3000, "Incorrect number of lines"
    for lin in lines:
        assert len(lin.split('|'))==2, "Invalid record format."
        assert lin == lin.lower()


def test_problem_1_11():
    pat = re.compile("|1$")
    filename = 'data/sentiment_lower_positive.psv'
    assert os.path.isfile(filename), "Missing output file."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 1500, "Incorrect number of lines"
    for lin in lines:
        assert len(lin.split('|'))==2, "Invalid record format."
        assert lin == lin.lower()
        assert pat.match(lin.strip()), f"Invalid data: {lin}."
    
    
def test_problem_1_12():
    pat = re.compile("|0$")
    filename = 'data/sentiment_lower_negative.psv'
    assert os.path.isfile(filename), "Missing output file."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 1500, "Incorrect number of lines"
    for lin in lines:
        assert len(lin.split('|'))==2, "Invalid record format."
        assert lin == lin.lower()
        assert pat.match(lin.strip()), f"Invalid data: {lin}."

        
def test_problem_1_13():
    pat = re.compile("|1$")
    filename = 'data/sentiment_positive.txt'
    assert os.path.isfile(filename), "Missing output file."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 1500, "Incorrect number of lines"
    for lin in lines:
        assert len(lin.split('|'))==1, "Invalid record format."
        assert lin == lin.lower()


def test_problem_1_14():
    pat = re.compile("|1$")
    filename = 'data/sentiment_negative.txt'
    assert os.path.isfile(filename), "Missing output file."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 1500, "Incorrect number of lines"
    for lin in lines:
        assert len(lin.split('|'))==1, "Invalid record format."
        assert lin == lin.lower()

        
def test_problem_1_15():
    filenames = [
        'data/sentiment_positive_tokens.txt',
        'data/sentiment_negative_tokens.txt'
    ]
    for fn in filenames:
        assert os.path.isfile(fn), f"Missing output file: {fn}."
        lines = open(fn, 'r', encoding='utf-8').readlines()
        for lin in lines:
            assert ' ' not in lin.strip(), "Invalid character."
        

def test_problem_1_16():
    pat = re.compile(r"^[\w]+")
    filenames = [
        'data/sentiment_positive_words.txt',
        'data/sentiment_negative_words.txt'
    ]
    for fn in filenames:
        assert os.path.isfile(fn), f"Missing output file: {fn}."
        lines = open(fn, 'r', encoding='utf-8').readlines()
        for lin in lines:
            llin = lin.strip()
            assert len(llin)==0 or pat.match(llin), f"Invalid character: `{llin}`."
            

def test_problem_1_17():
    word_list = ['990 the', '669 and', '466 a', '418 i', '417 is', '326 this',
                  '311 it', '308 of', '305 to', '257 was', '205 in', '198 great',
                  '176 good', '159 for', '157 with', '146 very', '126 that', '125 my',
                  '108 on', '102 are']
    filename = "output_1_17.txt"
    assert os.path.isfile(filename), f"Missing output file: {filename}."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 20, "Incorrect number of lines"
    pairs = zip(word_list, map(str.strip, lines))
    for p in pairs:
        assert p[0] == p[1], f"Mismatch: `{p[0]}` vs `{p[1]}`"
        

def test_problem_1_18():
    word_list = ['951 the', '469 i', '460 and', '420 a', '361 to', '354 it',
                 '336 is', '314 of', '313 this', '312 was', '250 not', '193 in',
                 '177 that', '177 for', '126 my', '116 with', '114 but',
                 '111 you', '111 on', '97 very']
    filename = "output_1_18.txt"
    assert os.path.isfile(filename), f"Missing output file: {filename}."
    lines = open(filename, 'r', encoding='utf-8').readlines()
    assert len(lines) == 20, "Incorrect number of lines"
    pairs = zip(word_list, map(str.strip, lines))
    for p in pairs:
        assert p[0] == p[1], f"Mismatch: `{p[0]}` vs `{p[1]}`"
        
        
def test_problem_1_19():
    
    def is_sorted(lines):
        freq_list = [ int(s.strip().split(' ')[0]) for s in lines ]
        freq_sort = sorted(freq_list, reverse=True)
        return all([ t[0] == t[1] for t in zip(freq_list, freq_sort) ])
    
    filenames = [
        'data/positive_words.lst',
        'data/negative_words.lst'
    ]
    for fn in filenames:
        assert os.path.isfile(fn), f"File does not exist: {fn}"
        lines = open(fn, 'r', encoding='utf-8').readlines()
        lines2 = list(filter(lambda s: len(s)>1, lines))
        assert is_sorted(lines2), "List is not sorted."
        
    
def test_problem_1_20():
    assert True, "No test"
    
    
def test_problem_1_21():
    assert True, "No test"
    
    
def test_problem_1_22():
    assert True, "No test"

    
def test_problem_1_23():
    assert True, "No test"

    
def test_problem_1_24():
    assert os.path.isfile('circle_area.py'), "File doesn't exist."


def test_problem_1_25():
    output = os.popen('echo "5" | ./circle_area.py').readlines()
    expected = [
        "This program calculates the area of a cricle for a given radius.",
        "π is defined as 3.141",
        "Enter the radius: The area of the circle is: 78.540"
        
    ]
    for j in range(3):
        assert output[j].strip().startswith(expected[j]), f"Mismatch in line {j+1}"



