# Assignment HW04
In this assignment we explore the Pandas library.

## Instructions
**Please following the instructions precisely!**

Create a file `hw4_answers.py` in this folder. You may use the file `hw4_template.py` as a template.

You can use the notebook `CheckHomework04.ipynb` to test your solution. (Note: the notebook will **not** be graded.)

### Problem 1
Create a function `load_employees` that loads the employees table from
the file  `/home/data/AdventureWorks/Employees.xls` and sets the index of the DataFrame to the `EmployeeID`. The function should return a table with the `EmployeeID` as the index and the remaining 25 columns.

### Problem 2
Define a function `getFullName` which takes the employees table and a single employee ID as arguments, and returns a string with the full name of the employee in the format "LAST, FIRST MIDDLE".
If the given ID does not belong to any employee return the string "UNKNOWN" (in all caps)
If no middle name is given only return "LAST, FIRST". Make sure there are not trailing spaces!
If only the middle initial is given the return the full name in the format "LAST, FIRST M." with the middle initial followed by a '.'.

Arguments:
- df (DataFrame): Employee Table
- empid (int):  Employee ID

Returns:
- String with full name

### Problem 3
Define a function `isSales` that takes the job title of an employee as string as an argument and return either `True` if the job title indicates this person works in sales, and `False` otherwise.

Argument:
- jobtitle (str)

Returns:
- True or False


### Problem 4
Define a function `filterSales` with the employee tables as an argument, that returns a new table of the same schema (i.e. columns and index) containing only row of sales people. You should use the `isSales` function from the previous problem.

Arguments:
- employees (DataFrame)

Returns:
- DataFrame with only people form the Sales Department


### Problem 5
Define a function `getEmailList` with that returns a Series of strings of all email addresses of employees in this state or province. The email addresses should be separated by a given character, usually a comma ',' or semicolon ';'.

Arguments:
- employees (DataFrame)
- delimiter (str)

Returns:
- Series of email addresses, concatenated by the given delimiter. The Series is indexed by the state or province.


### Problem 6 (Bonus)
Define a function `managementCounts` which produces a Series of how many employees report to a manager. The Series is indexed by the `ManagerID`, the count should be performed on the `EmployeeID` because this is the only field that is guaranteed to be unique. The resulting Series should be order by the number of employees in **descending order**.

Arguments:
- employees (DataFrame)

Returns:
- Series of counts (int), indexed by `ManagerID`

## Submission
The file `hw4_answers.py` must reside in this directory. Use the command

```homework MSA8010F17 HW04 check```

to see if the systems recognizes your homework solution.
