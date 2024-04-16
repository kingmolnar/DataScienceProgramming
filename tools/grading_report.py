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
T_now = datetime.datetime.now

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import argparse

from src.homework_grading import (
    summary_log,
    summary_grade,
    create_homework_report,
    load_icollege_users,
    create_icollege_import_table,
)

TS = datetime.datetime.now().strftime('%Y-%m-%d')

MAIN_DIR = os.path.dirname(os.path.dirname(__file__))
print(MAIN_DIR)

def main(assignment: str, max_points: int = None, points_per_problem: int = 2, with_date: bool = False):
    results_prefix = jp(MAIN_DIR, f'log/grades_{assignment}')
    latest_log = sorted(glob(f"{results_prefix}*"), reverse=True)[0]
    print(f"Latest log file: {latest_log}")
    assert os.path.isfile(latest_log), f"Log file `{latest_log}` does not exist!"
    
    hw = summary_log(latest_log, points_per_problem=points_per_problem)
    
    grad_path = jp(MAIN_DIR, 'private', 'grades')
    os.system(f"mkdir -p {grad_path}")
    
    name_suffix = f"{assignment}-{TS}" if with_date else assignment

    hw.to_excel(jp(grad_path, f"detailed-{name_suffix}.xlsx"), index=None)
    agg_hw = hw.groupby(['Assignment', 'User']) \
        .agg({
            'Passed': 'sum',
            'Failed': 'sum',
            'Errors': 'sum',
            'Warnings': 'sum',
            'Points': 'sum',
        }) \
        .reset_index()
    agg_hw.to_excel(jp(grad_path, f"summary-{name_suffix}.xlsx"), index=None)
    
    ### Create import file for iCollege
    dtol_user = load_icollege_users(jp(MAIN_DIR, 'private', 'PROGRAMMING'))
    dtol_import = create_icollege_import_table(dtol_user, agg_hw, assignment=assignment, max_points=max_points)
    dtol_import.to_csv(jp(grad_path, f"icollege-import-{name_suffix}.csv"), index=None)
    dtol_import.to_csv(jp(grad_path, f"icollege-import-{assignment}-{TS}.csv"), index=None)
    
    ### Report
    T_0 = T_now()
    for u in hw.User.dropna().drop_duplicates():
        print(f"User: {u}")
        if len(u)==0:
            continue
        rep = create_homework_report(hw, assignment=assignment, user=u)
        rep_path = jp(MAIN_DIR, 'private', 'report', u)
        os.system(f"mkdir -p {rep_path}")
        with open(jp(rep_path, f"report-{name_suffix}.md"), 'w', encoding='utf-8') as io:
            io.write(rep)
            io.write('\n')
    



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('ASSIGNMENT', help='ASSIGNMENT one of HW01, HW02, ...')
    parser.add_argument('-p', '--points-per-problem', type=int, default=2, help='Number of points per problem.')
    parser.add_argument('-m', '--max-points', type=int, default=0, help='Maximum number of points. No maximum if 0.')
    parser.add_argument('-t', '--with-date', action='store_true', help='Include date in file names.')
    args = parser.parse_args()

    print(TITLE)
    print(f"Assignment: {args.ASSIGNMENT}")

    main(args.ASSIGNMENT, max_points=args.max_points,
            points_per_problem=args.points_per_problem, with_date=args.with_date)
