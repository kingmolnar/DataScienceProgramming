# Solutions to homework 4
import numpy as np
import pandas as pd


#  ____            _     _                  _
# |  _ \ _ __ ___ | |__ | | ___ _ __ ___   / |
# | |_) | '__/ _ \| '_ \| |/ _ \ '_ ` _ \  | |
# |  __/| | | (_) | |_) | |  __/ | | | | | | |
# |_|   |_|  \___/|_.__/|_|\___|_| |_| |_| |_|
#
# Create a function `load_employees` that loads the employees table
# from the file  `/home/data/AdventureWorks/Employees.xls` and sets
# the index of the DataFrame to the `EmployeeID`.
# The function should return a table with the `EmployeeID` as the
# index and the remaining 25 columns.

def load_employees():
    pass ## fill int your code here


#  ____            _     _                  ____
# |  _ \ _ __ ___ | |__ | | ___ _ __ ___   |___ \
# | |_) | '__/ _ \| '_ \| |/ _ \ '_ ` _ \    __) |
# |  __/| | | (_) | |_) | |  __/ | | | | |  / __/
# |_|   |_|  \___/|_.__/|_|\___|_| |_| |_| |_____|
#
# Define a function `getFullName` which takes the employees table
# and a single employee ID as arguments, and returns a string with
# the full name of the employee in the format "LAST, FIRST MIDDLE".
# - If the given ID does not belong to any employee return the string
#     "UNKNOWN" (in all caps)
# - If no middle name is given only return "LAST, FIRST".
#     Make sure there are not trailing spaces!
# - If only the middle initial is given the return the full
#     name in the format "LAST, FIRST M." with the middle initial
#     followed by a '.'.
#
# Arguments:
# - df (DataFrame): Employee Table
# - empid (int):  Employee ID
#
# Returns:
# - String with full name

def getFullName(df, empid):
    pass ## fill int your code here

#  ____            _     _                  _____
# |  _ \ _ __ ___ | |__ | | ___ _ __ ___   |___ /
# | |_) | '__/ _ \| '_ \| |/ _ \ '_ ` _ \    |_ \
# |  __/| | | (_) | |_) | |  __/ | | | | |  ___) |
# |_|   |_|  \___/|_.__/|_|\___|_| |_| |_| |____/
#
# Define a function `isSales` that takes the job title of an
# employee as string as an argument and return either `True` if
# the job title indicates this person works in sales, and `False`
# otherwise.
#
# Argument:
# - jobtitle (str)
#
# Returns:
# - True or False

def isSales(jt):
    pass ## fill int your code here


#  ____            _     _                  _  _
# |  _ \ _ __ ___ | |__ | | ___ _ __ ___   | || |
# | |_) | '__/ _ \| '_ \| |/ _ \ '_ ` _ \  | || |_
# |  __/| | | (_) | |_) | |  __/ | | | | | |__   _|
# |_|   |_|  \___/|_.__/|_|\___|_| |_| |_|    |_|
#
# Define a function `filterSales` with the employee tables as an
# argument, that returns a new table of the same schema (i.e. columns
# and index) containing only row of sales people. You should use the
# `isSales` function from the previous problem.
#
# Arguments:
# - employees (DataFrame)
#
# Returns:
# - DataFrame with only people form the Sales Department


def filterSales(df):
    pass ## fill int your code here


#  ____            _     _                  ____
# |  _ \ _ __ ___ | |__ | | ___ _ __ ___   | ___|
# | |_) | '__/ _ \| '_ \| |/ _ \ '_ ` _ \  |___ \
# |  __/| | | (_) | |_) | |  __/ | | | | |  ___) |
# |_|   |_|  \___/|_.__/|_|\___|_| |_| |_| |____/
#
# Define a function `getEmailList` with that returns a Series of
# strings of all email addresses of employees in this state or
# province. The email addresses should be separated by a given
# character, usually a comma ',' or semicolon ';'.
#
# Arguments:
# - employees (DataFrame)
# - delimiter (str)
#
# Returns:
# - Series of email addresses, concatenated by the given delimiter.
#      The Series is indexed by the state or province.

def getEmailListByState(df):
    pass ## fill int your code here


#  ____            _     _                   __
# |  _ \ _ __ ___ | |__ | | ___ _ __ ___    / /_
# | |_) | '__/ _ \| '_ \| |/ _ \ '_ ` _ \  | '_ \
# |  __/| | | (_) | |_) | |  __/ | | | | | | (_) |
# |_|   |_|  \___/|_.__/|_|\___|_| |_| |_|  \___/
#
# Define a function `managementCounts` which produces a Series
# of how many employees report to a manager. The Series is indexed
# by the `ManagerID`, the count should be performed on the `EmployeeID`
# because this is the only field that is guaranteed to be unique.
# The resulting Series should be order by the number of employees
# in **descending order**.
#
# Arguments:
# - employees (DataFrame)
#
# Returns:
# - Series of counts (int), indexed by `ManagerID`

def managementCounts(df):
    pass ## fill int your code here
