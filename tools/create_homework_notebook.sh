#!/bin/bash
NUMBER="$1"

N_PROBLEMS="$2"
if [ -z "$N_PROBLEMS" ]; then
    N_PROBLEMS=25
fi

DUE_DATE="$3"


# HEADER
cat <<EOF
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Homework ${NUMBER}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%%sh\n",
    "mkdir -p test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Topic 1\n",
    "Review ..."
   ]
  },
EOF

# BODY

for (( N=1; N<=$N_PROBLEMS; N++ ))
do 
    cat <<EOF

  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### ${NUMBER}.${N} Problem Statement\n",
    "Instructions\n",
    "1. one\n",
    "2. two"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Save your solution to \`solution_${NUMBER}_${N}.py\`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%%writefile solution_${NUMBER}_${N}.py\n",
    "\n",
    "### your code here\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
      "# Try your code\n",
      "from solution_${NUMBER}_${N} import *\n",
      "\n",
      "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#### Test ${NUMBER}.${N} "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing test/test_${NUMBER}_${N}.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile test/test_${NUMBER}_${N}.py\n",
    "from solution_${NUMBER}_${N} import *\n",
    "\n",
    "def test_${NUMBER}_${N}():\n",
    "    assert True, \"No Test\""
   ]
  },
EOF
done

# FOOTER 

cat <<EOF
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Testing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%%sh\n",
    "python3 -m pytest"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Homework Submission\n",
    "- This homework is due by ${DUE_DATE}, 5:30PM (EDT)\n",
    "- Make sure that all your programs and output files are in the exact folder as specified in the instructions.\n",
    "- All file names on this system are case sensitive. Verify if you copy your work from a local computer to your home directory on ARC.\n",
    "- No further action is need to submit your assignment."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
EOF