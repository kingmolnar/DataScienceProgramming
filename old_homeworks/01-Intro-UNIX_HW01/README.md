# Assignment HW01
## Instructions
**Please following the instructions precisely!**

The goal of this homework is to familiarize you with the UNIX command line and to practice some basic commands that will be useful to your work in this class. To submit this homework, place all scripts and files in the DataScienceProgramming/01-Intro-UNIX/HW01 directory on the cluster by 11:55 PM on Mon 8/28/2017. Your homework will be collected precisely at midnight (using a shell script, of course!) If you have any questions about submitting the homework, please email the course instructors BEFORE THE DUE DATE.

To run your script, you may need to change the file permissions it has. You have to say that the script is allowed to execute code on your system. To do this, run `chmod +x [your filename]` in the directory where your file is located. For example, run `chmod +x question1.sh`. You can get more information about the chmod command by running "man chmod".

There are many nuances to deal with in shell scripting. We avoided dealing with most of the complexity in our brief introduction, but for those interested, you may find the following quick overview helpful: https://www.panix.com/~elflord/unix/bash-tute.html.

For this assignemt, you will use the files in /home/data/20_newsgroup/. DO NOT COPY the files to your home directory.

QUESTIONS:
1. In class, we talked about how you can use the "cd" command to change to a new directory, and how you can use "ls" to list all the files in that directory. You can also call the "ls" command with a directory name to list the files in that directory. The following is an example of a shell script that displays the name of the directory "/home/data/20\_newsgroup/" and lists the files in it: <br /> <br />
`#!/bin/bash` <br />
`echo "Contents of directory /home/data/20_newsgroup/:"` <br />
`ls /home/data/20_newsgroup/` <br /> <br />
Write a shell script called "question1.sh" that uses cd to change to the directory "/home/data/20_newsgroup/" and lists the contents of the directory "sci.crypt". Display only the first 10 files in the list (hint: use the "head" command!). Use the "pwd" command in the last line of your script to verify that you have changed directories.

2. The "grep" command can be used to search for a text string. Write a shell script called "question2.sh" that lists the contents of /home/data/20_newsgroup/ (regardless of where it is called from) and uses "grep" to display the names of the directories containing "sci" in the name (these are directories containing science-related articles). Also return a count of these directories. Use the following incompete shell script as a template: <br /> <br />
`#!/bin/bash` <br />
`echo "Science-related directories in /home/data/20_newsgroup/:"` <br />
`[your code here]` <br />
``echo "There are `[your code here]` directories containing articles related to science."`` <br /> <br />

3. Write a shell script called "question3.sh" by copying "question2.sh" (using cp) and adding the following line at the end (fill in the missing code too!): <br /> <br />
``"There are `[your code here]` directories NOT containing articles related to science."``

4. Another useful utility that we discussed in class was the "tr" command, which allows you to make single-character substitutions in text. In class, we did only single-character substitutions at a time; however, you can pass a set of values (or even a range) to substitute. For example, the following script (let's say it lives in a file called "myscript.py") will take text from the standard input and convert all uppercase characters to lowercase: <br /> <br />
`#!/bin/bash` <br />
`tr 'A-Z' 'a-z'` <br /> <br />
If we pass it text from a file by calling: <br />
`cat file.txt | ./myscript.sh` <br /> <br />
we will get all the text from file.txt, converted to lowercase. Write a shell script called "question4.sh" that does the following:
   1. Extracts all lines from the input text that contain the word "water"
   2. Converts all characters in those lines to lowercase
   3. Makes the text "leet", by substituting all "a" with "4", "t" with "7", "i" with "1", and "e" with "3".
   4. Writes the modified lines to a text file called "leetlines.txt"
   5. Displays the number of lines written to "leetlines.txt" using the command: echo "\`[your code here]\` lines written."
I will test your scipt by calling it with: <br /> <br />
`cat [filename] | ./question4.sh`

5. Write a script called "question5a.sh" that counts the number of occurences of the STRING "sing" in the text input (capitalization should not matter). Write another script called "question5b.sh" that counts the number of occurences of WORD "sing" in the text input (again, capitalization should not matter). I will test your script by calling it with: <br /> <br />
`cat [filename] | ./question5a.sh` <br />
`cat [filename] | ./question5b.sh`

6. BONUS. You can write more complicated shell scripts by using arguments and variables. The character "$" is used to get the value of a variable. Try doing "echo $PATH" in the command line. This tells you the value of the system variable PATH. Arguments in your script can be accessed in the order that they were passed, using $1 for the first argument, $2 for the second, etc. For example, the following script takes 3 inputs: first name, last name, and age: <br /> <br />
`#!/bin/bash` <br />
``echo "Hello! My name is $1 $2, and I am $3 years old."`` <br /> <br />
If you save the script as "myscript2.sh" and run "./myscript2.sh John Jones 26", it will output: "Hello! My name is John Jones, and I am 26 years old." <br />
Write a script called "question6.sh" that takes a file name and a text string as its first and second arguments, respectively, and counts the number of unique occurrences of the text string in the given file. Make sure that you are counting occurrences of the word, and not just matching lines! Case should not matter, and match whole words only (so if I call "question6.sh [filename] hat", I should get counts of the word "hat" and not of longer words that contain "hat" as a substring--for example, "that").  


## Submission due Friday September 1, 2017 at 12-noon
1. Save your scripts in this directory (where this README.md file resides)
2. Make sure that your script files are named exactly as indicated in the instructions. UNIX is case sensitive!!! (unlike MS Windows) Never, ever use spaces (blanks) in filenames!!!
3. Make your script files executable using the "chmod" command
4. A robot will pick up your file at the given deadline and evaluate it for assessment.
