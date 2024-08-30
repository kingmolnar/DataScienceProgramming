#!/usr/bin/env python3


import os
jp = os.path.join

import pandas as pd
import warnings

# PAWS_XLSX = '202401_21508_classlist.xlsx'
PAWS_XLSX = '202408_87953_classlist.xlsx'
PAWS_SKIP = 14
DIR_NAME = os.path.abspath(jp(os.path.dirname(__file__), '..', '..'))

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    df = pd.read_excel(jp(DIR_NAME, PAWS_XLSX), skiprows=PAWS_SKIP)

    print('\n'.join(df.Email.dropna().map(lambda s: s.split('@')[0], na_action='ignore').values))
