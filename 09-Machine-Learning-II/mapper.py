#!/usr/bin/python
import os
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import sklearn.tree
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support
import itertools
import json

def load_df(DATAFILE):
    df = pd.read_csv(DATAFILE, sep=';')
    all_features = set(df.columns)-set(['y'])
    num_features = set(df.describe().columns)
    cat_features = all_features-num_features
    level_substitution = {}

    def levels2index(levels):
        dct = {}
        for i in range(len(levels)):
            dct[levels[i]] = i
        return dct

    df_num = df.copy()

    for c in cat_features:
        level_substitution[c] = levels2index(df[c].unique())
        df_num[c].replace(level_substitution[c], inplace=True)

    ## same for target
    df_num.y.replace({'no':0, 'yes':1}, inplace=True)
    return df_num
    
    
    
if __name__ == "__main__":
    DATAFILE = '/home/data/archive.ics.uci.edu/BankMarketing/bank.csv'
    df_num = load_df(DATAFILE)
    y = df_num.y.as_matrix()
    
    nams = [b for a in ['Precision', 'Recall', 'F1_score', 'Support'] for b in ['%s_no'%a, '%s_yes'%a]]
    
    for line in sys.stdin:
        line = line.strip()
        MaxDepth, Nftrs, ftrs = line.split(',', 2)
        MaxDepth = int(MaxDepth)
        Nftrs = int(Nftrs)
        features = ftrs.split(',')
        X = df_num[features].as_matrix()
        clf = DecisionTreeClassifier(max_depth=MaxDepth)
        perf_arr = None    #-- this array will hold results for different random samples
        for i in range(10): ### running train and test on different random samples
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=i)
            
            clf.fit(X_train, y_train)
            y_hat = clf.predict(X_test)
            #Prec, Recall, F1, Supp 
            prf1s = precision_recall_fscore_support(y_test, y_hat)

            if type(perf_arr)!=type(None):
                perf_arr = np.vstack((perf_arr, np.array(prf1s).reshape(1,8)))
            else:
                perf_arr = np.array(prf1s).reshape(1,8)

        perf_agg = perf_arr.mean(axis=0)  #-- mean over rows, for each column
        perf = {}
        perf['MaxDepth'] = MaxDepth
        perf['Nftrs'] = Nftrs
        perf['Features'] = list(features)
        for i in range(8):
            perf[nams[i]] = perf_agg[i]
        
        print(json.dumps(perf))
 