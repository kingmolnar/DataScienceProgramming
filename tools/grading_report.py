#!/usr/bin/env python3
TITLE = r"""
   ____               _ _               ____                       _   
  / ___|_ __ __ _  __| (_)_ __   __ _  |  _ \ ___ _ __   ___  _ __| |_ 
 | |  _| '__/ _` |/ _` | | '_ \ / _` | | |_) / _ \ '_ \ / _ \| '__| __|
 | |_| | | | (_| | (_| | | | | | (_| | |  _ <  __/ |_) | (_) | |  | |_ 
  \____|_|  \__,_|\__,_|_|_| |_|\__, | |_| \_\___| .__/ \___/|_|   \__|
                                |___/            |_|                   

"""
from typing import Any
import sys
import os
jp = os.path.join

from glob import glob
import re
import json
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from src.homework_grading import (
    summary_log,
    summary_grade,
    create_homework_report,
)

TS = datetime.datetime.now().strftime('%Y-%m-%d')

MAIN_DIR = os.path.dirname(os.path.dirname(__file__))
print(MAIN_DIR)

def main(assignment):
    RESULTS_PREFIX = jp(MAIN_DIR, f'log/grades_{assignment}')
    latest_log = sorted(glob(f"{RESULTS_PREFIX}*"), reverse=True)[0]
    print(f"Latest log file: {latest_log}")
    assert os.path.isfile(latest_log), f"Log file `{latest_log}` does not exist!"
    
    hw = summary_log(latest_log, points_per_problem=2)
    
    grad_path = jp(MAIN_DIR, 'private', 'grades')
    os.system(f"mkdir -p {grad_path}")
    
    hw.to_excel(jp(grad_path, f"detailed-{assignment}-{TS}.xlsx"), index=None)
    agg_hw = hw.groupby(['Assignment', 'User']) \
        .agg({
            'Passed': 'sum',
            'Failed': 'sum',
            'Errors': 'sum',
            'Warnings': 'sum',
            'Points': 'sum',
        }) \
        .reset_index()
    agg_hw.to_excel(jp(grad_path, f"summary-{assignment}-{TS}.xlsx"), index=None)
    
    for u in hw.User.dropna().drop_duplicates():
        print(f"User: {u}")
        if len(u)==0:
            continue
        rep = create_homework_report(hw, assignment=assignment, user=u)
        rep_path = jp(MAIN_DIR, 'private', 'report', u)
        os.system(f"mkdir -p {rep_path}")
        with open(jp(rep_path, f"report-{assignment}-{TS}.md"), 'w', encoding='utf-8') as io:
            io.write(rep)
            io.write('\n')
    



if __name__ == '__main__':
    if len(sys.argv)>1:
        print(TITLE)
        assignment = sys.argv[1].strip()
        print(f"Assignment: {assignment}")
        main(assignment)
    else:
        print(f"Usage: {os.path.basename(__file__)} ASSIGNMENT\n")
        print(f"       whith ASSIGNMENT one of HW01, HW02, ...")
