import sys
import os
jp = os.path.join

hw_dir = "IFI8410F23/DataScienceProgramming/Homework/HW06"
mesg = """
========================================================================================================
========================================================================================================
===                                                                                                  ===
===    WRONG DIRECTORY !!!                                                                           ===
===    Your homework solutions are not in the proper directory.                                      ===
===                                                                                                  ===
===    Unless you move your homework solutions to the directory as instructed in the assignment,     ===
===    your homework WILL NOT BE GRADED.                                                             ===
===                                                                                                  ===
========================================================================================================
========================================================================================================
"""

def test_6_0():
    wd = os.getcwd()
    home_dir = os.getenv('HOME')
    assert jp(home_dir, hw_dir) == wd, mesg
    
