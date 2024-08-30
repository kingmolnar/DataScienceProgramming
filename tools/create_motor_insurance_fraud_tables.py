#!/usr/bin/env python3

import numpy as np
import pandas as pd
import os
jp = os.path.join
from glob import glob

SOURCE_DATA = '/data/kelleher/MotorInsuranceFraudClaimABTFull.csv'
TABLE_DIR = '/data/kelleher'
TABLE_PREFIX = 'MotorInsuranceFraudClaim'

def main(source_csv, dest_dir, prefix):
    df = pd.read_csv(source_csv)
    df.rename(lambda c: str(c).strip().replace(' ', '').replace('%', 'Percent'), inplace=True, axis=1)
    
    # Save clean version
    df.to_csv(jp(dest_dir, f'{prefix}_clean.csv'), index=None)
    
    # Save single columns for numeric
    for col in ['ClaimAmount', 'TotalClaimed', 'NumClaims', 'NumSoftTissue', 'PercentSoftTissue', 'ClaimAmountReceived']:
        df[[col]].to_csv(jp(dest_dir, f'{prefix}_{col}.csv'), index=None, header=None)
    
    
    # Save single columns for categorical
    for col in ['InsuranceType', 'IncomeofPolicyHolder', 'MaritalStatus']:
        df[[col]].to_csv(jp(dest_dir, f'{prefix}_{col}.csv'), index=None, header=None)
            
    # Save two columns
    df[['ClaimAmount', 'ClaimAmountReceived']] \
        .to_csv(jp(dest_dir, f'{prefix}_Claimed_vs_Received.csv'), index=None, header=None)
    
    print("Data Files:")
    
    for file in glob(jp(dest_dir, f'{prefix}_*.csv')):
        print(file)
        
if __name__ == '__main__':
    main(SOURCE_DATA, TABLE_DIR, TABLE_PREFIX)
