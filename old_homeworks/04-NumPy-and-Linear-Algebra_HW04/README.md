# Assignment HW03
## Instructions
**Please following the instructions precisely!**

For this homework, you will be using the "Cameras" dataset, which can be downloaded in csv form from: 
<p style="text-align: center;">https://perso.telecom-paristech.fr/eagan/class/igr204/datasets</p> 
On the cluster, you can do: </br>

`wget https://perso.telecom-paristech.fr/eagan/class/igr204/data/Camera.csv`</br>

The file includes model names and some numeric attributes for about 1000 cameras. Dealing with mixed-type data (strings and numeric values) in numpy is actually a little challenging, so we'll replace the model names with numbers. To do this, use the script "preprocess_data.sh" included in this folder. First, change permissions for the script: </br>

`chmod +x preprocess_data.sh` </br>

Next, run the script to remove model names and save the result to a new file, "Cameras_noname.csv": </br>

`./preprocess_data.sh Camera.csv Camera_noname.csv`

Use "Camera_noname.csv" to answer the following questions. Be sure to examine the dataset using command line arguments first!

To submit your assignment, write all your functions in the indicated spaces in the Jupyter notebook called "HW3_submission.ipynb" located in this directory. Run the notebook to generate a .py file that will make up your submission.

1. Write a function called "load_data" that takes as its one argument the data file name, and returns a numpy nd-array with the data. Assume that the data file is in the same format as Camera_noname.csv (one-line header, all numeric data). You may want to check out numpy.loadtxt. NOTE: "import numpy as np" is already included in the file header. 

2. Write a function called "count_new" that takes as its one argument the nd-array produced in question 1 and returns the number of cameras were released after 1999 (2000 and on).

3. Write a function called "get_heaviest_new" that takes as its one argument the nd-array produced in question 1 and returns the Model ID (first column in dataset) of the heaviest camera released after 1999 (weight includes batteries). (Note: data may contain "nan" values and non-physical weights--your functions should be able to handle that!)

4. Write a function called "price_summary_new" that takes as its one argument the nd-array produced in question 1 and returns the mean price of a camera released after 1999, as well as the min and max price in this group. Your output should be a tuple of (mean price after 1999, lowest price after 1999, highest price after 1999). 

5. It's always a good idea to examine your data and make sure that all the values make sense. Write a function called "bad_resolution" that takes as its one argument the nd-array produced in question 1 and returns the number of non-reasonable (nan or out of range) values for the max resolution. 

6. (Bonus) Write a function called "resolution_fit" that takes as its one argument the nd-array produced in question 1 and returns a tuple (a, b) corresponding to the linear fit coefficients y = a x + b, where x is release date and y is max resolution (your function should ignore any non-physical values in the release date and max resolution). 

## Submission
