#!/bin/bash
CLASS_DIR=IFI8410F23
GIT_REPO=https://github.com/kingmolnar/DataScienceProgramming.git
GIT_DIR=DataScienceProgramming

cat private/ifi8410_users.log | while read U S D
do
        echo $U
        HOME_DIR=/home/$U
        su - $U -c "mkdir -p $HOME_DIR/$CLASS_DIR"
        if [ ! -d $HOME_DIR/$CLASS_DIR/$GIT_DIR ]
        then
                su - $U -c "cd $HOME_DIR/$CLASS_DIR ; git clone $GIT_REPO"
                echo "Clone GIT repo"
        else
                echo "Pull GIT repo"
                ## su - $U -c "cd $HOME_DIR/$CLASS_DIR/$GIT_DIR ; git config pull.rebase false"
                su - $U -c "cd $HOME_DIR/$CLASS_DIR/$GIT_DIR ; git stash; git pull; git stash pop"
                ## su - $U -c "cd $HOME_DIR/$CLASS_DIR/$GIT_DIR ; git pull"
        fi
done
echo "Done."
