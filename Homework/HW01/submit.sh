#!/usr/bin/bash

SUBMISSION="/data/IFI8410/submissions/P24"
RLP=`realpath $0`
DIR=`dirname $RLP`
HW=`basename $DIR`
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

mkdir -p "$DEST/data"
cat <<EOF | while read F; do if [ -f "$F" ]; then echo ".....SUBMIT '$F'"; cp -a $F "$DEST/data"; else echo "!!! MISSING '$F' !!!"; fi; done
data/joined_words.lst
data/negative_words_alphabetic_order.lst
data/negative_words.lst
data/positive_negative_table.csv
data/positive_words_alphabetic_order.lst
data/positive_words.lst
data/sentiment_lower_negative.psv
data/sentiment_lower_positive.psv
data/sentiment_lower.psv
data/sentiment_negative_tokens.txt
data/sentiment_negative.txt
data/sentiment_negative_words.txt
data/sentiment_positive_tokens.txt
data/sentiment_positive.txt
data/sentiment_positive_words.txt
data/sentiment.psv
data/sentiment.tsv
data/top_100_negative_words.lst
data/top_100_positive_words.lst
data/word_frequency_positive_negative.csv
EOF

cat <<EOF | while read F; do if [ -f "$F" ]; then echo ".....SUBMIT '$F'"; cp -a $F "$DEST/"; else echo "!!! MISSING '$F' !!!"; fi; done
output_1_17.txt
output_1_18.txt
output_1_2.txt
output_1_3.txt
output_1_4.txt
output_1_5.txt
output_1_6.txt
output_1_7.txt
EOF