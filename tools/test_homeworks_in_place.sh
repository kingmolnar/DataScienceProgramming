#!/bin/bash
MAIN_DIR="`dirname $0`/.."
CLASS_DIR=IFI8410F23
GIT_REPO=https://github.com/kingmolnar/DataScienceProgramming.git
GIT_DIR=DataScienceProgramming
ASSIGNMENT="01-Intro-UNIX/HW01"

cat $MAIN_DIR/private/ifi8410_users.log | while read U S D
do
        echo $U
        HOME_DIR=/home/$U
        if [ -d $HOME_DIR/$CLASS_DIR/$GIT_DIR/$ASSIGNMENT ]
        then
            printf "$ASSIGNMENT\t$U\tTEST START\n"
            su - $U -c "cd $HOME_DIR/$CLASS_DIR/$GIT_DIR/$ASSIGNMENT; pytest" 2>&1 | awk "{print \"$ASSIGNMENT\t$U\t\", \$0}"
            printf "$ASSIGNMENT\t$U\tTEST END\n\n"
        else
            printf "$HOME_DIR/$CLASS_DIR/$GIT_DIR/$ASSIGNMENT\t$U\tNO ASSIGNMENT\n\n"
        fi
done
echo "Done."
