#!/usr/bin/env python3.4

import pandas as pd
import itertools

DATAFILE = '/home/data/archive.ics.uci.edu/BankMarketing/bank.csv'
MAX_DEPTH = '5,10'
N_FEATURE = '5,14'

NITER = 20

def spl_range(X):
    v = [int(t) for t in X.split(',')]
    return range(v[0], v[1]+1)

if __name__ == '__main__':
    maxdepth = MAX_DEPTH.split(',')
     
    df = pd.read_csv(DATAFILE, sep=';')
    all_features = set(df.columns)-set(['y'])
    num_features = set(df.describe().columns)
    cat_features = all_features-num_features
    use_features = all_features-set(['day', 'month'])
    
    #print("All features:         ", ", ".join(all_features)
    #      , "\nNumerical features:   ", ", ".join(num_features)
    #      , "\nCategorical features: ", ", ".join(cat_features))
   
    for MaxDepth in spl_range(MAX_DEPTH):  ###range(5,9):
        for Nftr in spl_range(N_FEATURE): ###[len(all_features) - k for k in range(len(all_features)-2))]:
            for ftrs in itertools.combinations(use_features, Nftr):
                lst = [str(MaxDepth), str(Nftr)] + list(ftrs)
                print(','.join(lst))
                