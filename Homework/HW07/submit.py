#  ____        _               _         _             
# / ___| _   _| |__  _ __ ___ (_)___ ___(_) ___  _ __  
# \___ \| | | | '_ \| '_ ` _ \| / __/ __| |/ _ \| '_ \ 
#  ___) | |_| | |_) | | | | | | \__ \__ \ | (_) | | | |
# |____/ \__,_|_.__/|_| |_| |_|_|___/___/_|\___/|_| |_|
#                                                      
#!!!!!                                            !!!!!
#!!!!!      DO NOT DELETE OR MODIFY THIS FILE     !!!!!
#!!!!!                                            !!!!!
import os
jp = os.path.join
import sys
import json
import ipykernel
import shutil

SUBMISSION = "/data/IFI8410/submissions/P24"

DIR = os.path.dirname(__file__)
HW = os.path.basename(DIR)
USER = os.getenv('USER')
DEST = jp(SUBMISSION, USER, HW)
# assert os.path.isdir(DEST), f'Submission folder {DEST} does not exist!'


def submit():
    if HW == ".":
        raise Exception(f"Invalid assignment '{HW}'")


    if not os.path.isdir(DEST):
        print("""
        *********************************************
        *     DESTINATION FOLDER DOES NOT EXIST     *
        *********************************************
 
        You can only submit your assignment on ARC.
        Complete your work on the designated system.
        """)
        exit(5)

    if not os.access(DEST, os.W_OK):
        print("""
        *********************************************
        *             SUBMISSION CLOSED             *
        *********************************************
        
        You no longer have write access to this folder.
        """)
        exit(5)
    
    info = json.loads(ipykernel.get_connection_info())
    notebook_name = os.path.basename(info['jupyter_session'])
    notebook_file = jp(os.getcwd(), notebook_name)
    print(f"Submit {notebook_file} to {DEST}")
    shutil.copy(notebook_file, DEST)
    
