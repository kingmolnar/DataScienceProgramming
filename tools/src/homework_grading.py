#  ██████╗ ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗                    
# ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝                    
# ██║  ███╗██████╔╝███████║██║  ██║██║██╔██╗ ██║██║  ███╗                   
# ██║   ██║██╔══██╗██╔══██║██║  ██║██║██║╚██╗██║██║   ██║                   
# ╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝                   
#  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝                    
                                                                          
# ███████╗██╗   ██╗███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
# ██╔════╝██║   ██║████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
# █████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
# ██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
# ██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
# ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝

from typing import Any, Tuple
from glob import glob
import re
import json
import datetime
import numpy as np
import pandas as pd

pat_failed = re.compile(r'([\d]+) failed')
pat_passed = re.compile(r'([\d]+) passed')
pat_errors = re.compile(r'([\d]+) error[s]{0,1}')
pat_warnings = re.compile(r'([\d]+) warning[s]{0,1}')

pat1 = re.compile(r"= (\d+) failed, (\d) passed in")
pat2 = re.compile(r"= (\d+) failed in")
pat3 = re.compile(r"= (\d+) passed in")


def split_line(row: str) -> Tuple[str, str, str, str]:
    tup = row.strip().split('\t', 4)
    if len(tup)==4:
        return tup[0], tup[1], tup[2], tup[3].strip()
    if len(tup)==3:
        return tup[0], tup[1], tup[2], ""
    if len(tup)==2:
        return tup[0], tup[1], "test", ""
    return "", "", "", ""
    

def extract_pass_fail(row):
    
    if res := pat_failed.search(row.Comment):
        n_failed = int(res.group(1))
    else:
        n_failed = 0
        
    if res := pat_passed.search(row.Comment):
        n_passed = int(res.group(1))
    else:
        n_passed = 0
        
    if res := pat_errors.search(row.Comment):
        n_errors = int(res.group(1))
    else:
        n_errors = 0
        
    if res := pat_warnings.search(row.Comment):
        n_warnings = int(res.group(1))
    else:
        n_warnings = 0
    
    return {
        'RowNumber': row.RowNumber,
        'Assignment': row.Assignment,
        'User': row.User,
        'Test': row.Test,
        'Passed': n_passed,
        'Failed': n_failed,
        'Errors': n_errors,
        'Warnings': n_warnings,
    }
    
    

def summary_log(filename: str, points_per_problem: int = 1) -> pd.DataFrame:
    results = open(filename, "r", encoding='utf-8').readlines()
    print(f"Number or log lines: {len(results):,}")
    
    df = pd.DataFrame(map(split_line, results),
                      columns=['Assignment', 'User', 'Test', 'Comment'])
    df['RowNumber'] = range(df.shape[0])
    df['NextUser'] = df.User.shift(-1)
    df['NextTest'] = df.Test.shift(-1)
    # df_summary = df[df.User!=df.NextUser]
    df_summary = df[(df.User!=df.NextUser)|(df.Test!=df.NextTest)]
    
    df_grades = pd.DataFrame.from_records(
        df_summary.apply(extract_pass_fail, axis=1).values)
    
    df_grades.sort_values(['User', 'Test'], inplace=True)
    df_grades['Points'] = df_grades.Passed * points_per_problem
    df_grades[df_grades.Test.str.endswith('_0')|df_grades.Test.str.contains('zero')]['Points'] = 0
    print(f"Number of graded records: {df_grades.shape[0]}")
    return df_grades
    
    
    
    
def summary_grade(hw_df: pd.DataFrame) -> pd.DataFrame:
    gr_df = hw_df.groupby(['Assignment', 'User']) \
    .agg({
        'Passed': 'sum',
        'Failed': 'sum',
        'Errors': 'sum',
        'Warnings': 'sum',
        'Points': 'sum',
    }) \
    .reset_index()
    return gr_df


def create_homework_report(log_df: pd.DataFrame, assignment: str, user: str, bins=5,
                            points_per_problem: int = None, max_points: int = None) -> str:
    output = ""
        
    hw_df = log_df[log_df.Assignment==assignment].drop('RowNumber', axis=1)
    sub_df = hw_df[hw_df.User==user]
    
    output += str(f"# Homework {assignment} for {user}\n\n")
    output += str("Report generated on {}\n".format(datetime.datetime.now().strftime('%Y-%m-%d')))
    if points_per_problem:
        output += str(f"Number of points per problem: {points_per_problem}\n")
    if max_points:
        output += str(f"Maximum number of points: {max_points}\n")
    output += str("\n")

    agg_df = sub_df.agg({
            'Passed': 'sum',
            'Failed': 'sum',
            'Errors': 'sum',
            'Warnings': 'sum',
            'Points': 'sum',    
        }).reset_index()
    agg_df.columns = ['Summary', 'Value']
    output += str(
           agg_df.to_markdown(index=None)
    )

    
    output += str("\n\n## Detailed Summary of Your Assignment\n\n")
    output += str(sub_df.drop(['Assignment', 'User'], axis=1).to_markdown(index=None))

    ## class summary

    class_df = hw_df[hw_df.Assignment==assignment] \
        .groupby(['Assignment', 'User', 'Test']) \
        .agg({
            'Passed': 'sum',
            'Failed': 'sum',
            'Errors': 'sum',
            'Warnings': 'sum',
            'Points': 'sum',
        }) \
        .reset_index()

    points = class_df.groupby('User').agg({'Points': 'sum'})
    vals, edges = np.histogram(points, bins=bins)
    
    class_distr = pd.DataFrame(
        [ (int(edges[j]), int(edges[j+1]), vals[j]) for j in range(len(vals)) ],
        columns=['From (Points)', 'To (Points)', 'Count']
        ).sort_index(ascending=False)
           
    output += str("\n\n## Class Distribution\n\n")
    output += str(class_distr.to_markdown(index=None))


           
    class_by_test = class_df.groupby('Test') \
        .agg({
            'Passed': 'sum',
            'Failed': 'sum',
            'Errors': 'sum',
            'Warnings': 'sum',
        }) \
        .reset_index()

    output += str("\n\n## Class Distribution by Exercise\n\n")
    output += str(class_by_test.to_markdown(index=None))
    output += "\n\n"
    return output
    
    

