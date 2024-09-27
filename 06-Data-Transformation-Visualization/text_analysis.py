# ████████╗███████╗██╗  ██╗████████╗     █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗██╗███████╗
# ╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝    ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝██╔════╝██║██╔════╝
#    ██║   █████╗   ╚███╔╝    ██║       ███████║██╔██╗ ██║███████║██║   ╚████╔╝ ███████╗██║███████╗
#    ██║   ██╔══╝   ██╔██╗    ██║       ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝  ╚════██║██║╚════██║
#    ██║   ███████╗██╔╝ ██╗   ██║       ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████║██║███████║
#    ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝╚══════╝
                                                                                                 
from typing import List, Dict, Tuple
from glob import glob
import os
import re
import math

def load_customer_review_data(files:str) -> List[Tuple[str, int]]:
    """Load customer review data. Data file has one review per line.
    Line contains text and sentiment (0=negative, 1=positive), split by '|'

    Args:
        files (str): File name

    Returns:
        List[Tuple[str, int]]: List of reviews in file as tuples.
                               First element is text, second is sentiment
    """
    file_list = glob(files)
    data = []
    for file in file_list:
        if os.path.isfile(file):
            for dat in open(file):
                tup = dat.split('\t')
                data.append((tup[0].strip(), int(tup[1])))
    return data


def split_by_sentiment(corpus: List[Tuple[str, int]], sentiment: int) -> List[str]:
    """Filter list of reviews (with sentiment) to a list of the reviews for given sentiment.
    The sentiment is either 0 or 1.
 
    Args:
        corpus (List[Tuple[str, int]]): List of reviews after processed with `load_customer_review_data()`
        sentiment (int): 0 for negative, 1 for positive

    Returns:
        List[str]: List of select review texts
    """
    assert sentiment in [0, 1], f"Sentiment must be 0 or 1. You provided: {sentiment}"
    return [ t[0] for t in corpus if t[1] == sentiment ]
    

def convert_to_token_list(rawtxt: str) -> List[str]:
    """Convert text to a list of tokens.
    All special characters, white-spaces, and digits are removed.
    The resulting tokens are in lower case.

    Args:
        rawtxt (str): Original (raw) text

    Returns:
        List[str]: List of tokens
    """
    txt1 = rawtxt.lower()
    txt1 = re.sub(r'\W', ' ', txt1)
    txt1 = re.sub(r'\d', ' ', txt1)
    txt1 = re.sub(r'\s+', ' ', txt1)
    return txt1.split()


def term_count(doc: List[str]) -> Dict[str, float]:
    """Count occurance of each token in document

    Args:
        doc (List[str]): Document in form of token list

    Returns:
        Dict[str, float]: Token and the number of times it appears in the document
    """
    f_td = {}
    for tok in doc:
        f_td[tok] = f_td.get(tok, 0) + 1
    return f_td


def term_frequency(doc: List[str]) -> Dict[str, float]:
    """Count (relative) frequency of token in document.
    Relative to the number of tokens in document.

    Args:
        doc (List[str]): Document in form of token list

    Returns:
        Dict[str, float]: Token and relative frequency in the document
    """
    f_td = term_count(doc)
    sum_f_td = sum(f_td.values())
    return { tok: (freq/sum_f_td) for tok, freq in f_td.items() } 

# """
#     # {'it': 0.05555555555555555,
#     #  'feels': 0.05555555555555555,
#     #  'more': 0.05555555555555555,
#     #  'comfortable': 0.05555555555555555,
#     #  'than': 0.05555555555555555,
#     #  'most': 0.05555555555555555, ...
#     """

def inverse_doc_frequency(corpus: List[List[str]]) -> Dict[str, float]:
    """Computes inverse of the number of time a term appears in documents

    Args:
        corpus (List[List[str]]): List of documents. Each document is a list of tokens.

    Returns:
        Dict[str, float]: Tokens and their inverse document frequency
    """
    N = len(corpus)
    numdocs = {}
    for doc in corpus:
        tcnt = term_count(doc)
        for tok in tcnt.keys():
            numdocs[tok] = numdocs.get(tok, 0) + 1
    return { tok: math.log(N/(1+cnt)) for tok, cnt in numdocs.items() }
    
    
    
def tfidf_from_corpus(corpus: List[List[str]]) -> List[Dict[str, float]]:
    """Computes TF-IDF for a list of documents

    Args:
        docs (List[List[str]]): Corpus, list of token lists

    Returns:
        List[Dict[str, float]]: List of documents, tokens with TF-IDF
   
    Example:
        [{'value': 1.341827559508747,
        'case': 1.0671744873417197,
        'excellent': 0.8453486885914939,
        'good': 0.5473141019217607},
        {'jawbone': 1.4817315064926027,
        'for': 0.5806969500778912,
        'great': 0.512632549546354,
        'the': 0.20036876436139342}, ...
    """
    idf_data = inverse_doc_frequency(corpus)
    res = []
    for doc in corpus:
        tf = term_frequency(doc)
        tfidf = { tok: freq * idf_data[tok] for tok, freq in tf.items() }
        tfidf_sorted = { x[0]: x[1] for x in sorted(tfidf.items(), key=lambda t: -t[1]) }
        res.append(tfidf_sorted)
    return res