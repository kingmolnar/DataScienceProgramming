#!/usr/bin/bash
#  ____        _               _         _             
# / ___| _   _| |__  _ __ ___ (_)___ ___(_) ___  _ __  
# \___ \| | | | '_ \| '_ ` _ \| / __/ __| |/ _ \| '_ \ 
#  ___) | |_| | |_) | | | | | | \__ \__ \ | (_) | | | |
# |____/ \__,_|_.__/|_| |_| |_|_|___/___/_|\___/|_| |_|
#                                                      
# Version 2, reluctantly allows blanks in file names...
#!!!!!                                            !!!!!
#!!!!!      DO NOT DELETE OR MODIFY THIS FILE     !!!!!
#!!!!!                                            !!!!!


SUBMISSION="/data/IFI8410_submissions/F24"
RLP=`realpath "$0"`
DIR=`dirname "$RLP"`
HW=`basename "$DIR"`
DEST="$SUBMISSION/$USER/$HW"

if [ "$HW" == "." ]
then
    echo "Invalid assignment '$HW'"
    exit 5
fi


##
## Test access
##
if [ ! -d $DEST ]
then
    echo "*********************************************"
    echo "*     DESTINATION FOLDER DOES NOT EXIST     *"
    echo "*********************************************"
    echo 
    echo "You can only submit your assignment on ARC."
    echo "Complete your work on the designated system."
    echo
    exit 5
fi


if [ ! -w $DEST ]
then
    echo "*********************************************"
    echo "*             SUBMISSION CLOSED             *"
    echo "*********************************************"
    echo 
    echo "You no longer have write access to this folder."
    echo
    exit 5
fi
    
    
##
## Ask for confirmation
##
cat <<EOF
*******************************************
*  You are about to submit Homework $HW  *
*******************************************

Any files that you previously submitted will
be overwritten by your current files.

EOF

if [ "$1" != "-y" ]
then 
    echo "Do you wish to continue? (enter the number of your choice)"
    select yn in "Yes" "No"; do
        case $yn in
            Yes ) break;;
            No )  exit;;
        esac
    done
fi

##
## Copy files
##

#mkdir -p "$DEST/data"
#cat <<EOF | while read F; do if [ -f "$F" ]; then echo ".....SUBMIT '$F'"; cp -a $F "$DEST/data"; else echo "!!! MISSING '$F' !!!"; fi; done
#EOF

cat <<EOF | while read F; do if [ -f "$F" ]; then echo ".....SUBMIT '$F'"; cp -a $F "$DEST/"; else echo "!!! MISSING '$F' !!!"; fi; done
solution_11_1.py
solution_11_2.py
EOF

cat <<EOF | while read F; do if [ -f "$F" ]; then echo ".....SUBMIT '$F'"; cp -a $F "$DEST/"; else echo "!!! MISSING '$F' !!!"; fi; done
ahc_clustering_average.png
dbscan_blobs_and_rings.png
comparison_of_clustering_techniques.png
EOF

echo
echo "Submission completed. Check your assignments if you see any files marked as  !!! Missing !!!"
