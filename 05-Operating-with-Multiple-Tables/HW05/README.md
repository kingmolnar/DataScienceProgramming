# Assignment HW05
## Instructions
**Please following the instructions precisely!**


Create a file `hw5_answers.py` in this folder. You may use the file `hw4_template.py` as a template.

You can use the notebook `CheckHomework05.ipynb` to test your solution. (Note: the notebook will **not** be graded.)
For this assignment, you will be working with the AdventureWorks dataset that we studied in class. You don't need to copy the dataset into your home directory, you can import it directly from files in the /home/data/AdventureWorks/ directory. 

<!-- Please use the HW05_Submission Jupyter notebook to complete your assignment. This notebook will generate hw5_answers.py, which will be the file submitted for grading.
-->

The Employees, Territory, Customers, and Orders tables are the same as those we used in class.

1. Write a function called `get_manager` that takes as its one argument the Pandas DataFrame "Employees" and returns a DataFrame containing list of all employees (EmployeeID, first name, middle name, last name), and their manager's first and last name. The columns in the output DataFrame should be: EmployeeID, FirstName, MiddleName, LastName, ManagerFirstName, ManagerLastName.

2. Write a functon called `get_spend_by_order` that takes as its two arguments the Pandas DataFrames "Orders" and "Customers", and returns a DataFrame with the following columns: "FirstName", "LastName",  "Item", "TotalSpent", listing all cutomer names, their purchased items, and the total amount spend on that item (remember that the "Price" listed in "Orders" is the _price per item_).

3. Write a function called `get_order_location` that takes three arguments: "Orders", "Customers", and "Territory", and returns a DataFrame containing the following columns: "CustomerID", "Name", and "TotalItems", that gives, for each order, the ~OrderID~ CustomerID, the name of the territory where the order was placed, and the total number of items ordered (yes, 2 ski poles counts as 2 items). 

4. Write a function called `employee_info` that takes one argument: "Employees", and returns a DataFrame containing the following columns: JobTitle, NumberOfEmployees, and MeanVacationHours, containing all job titles, the number of employees with that job title, and the mean number of vacation days for employees with that job title. 

## Submission
Place the file `hw5_answers.py` in this directory.
