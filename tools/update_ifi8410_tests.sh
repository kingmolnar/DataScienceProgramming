#!/bin/bash
CLASS_DIR=IFI8410F23
GIT_REPO=https://github.com/kingmolnar/DataScienceProgramming.git
GIT_DIR=DataScienceProgramming
HW_DIR=Homework
cat private/ifi8410_users.log | while read U S D
do
        echo $U
        HOME_DIR=/home/$U
        TARGET_DIR=$HOME_DIR/$CLASS_DIR/$GIT_DIR/$HW_DIR

        # su - $U -c "mkdir -p $TARGET_DIR"
        if [ ! -d $HOME_DIR/$CLASS_DIR/$GIT_DIR ]
        then
                su - $U -c "mkdir $HOME_DIR/$CLASS_DIR ; git clone $GIT_REPO"
                echo "Clone GIT repo"
        else
                su - $U -c "mkdir -p $TARGET_DIR"
                echo "Update test scripts"
                for H in HW02
                do
                        cp -a /home/pmolnar/$CLASS_DIR/$GIT_DIR/$HW_DIR/$H/test $TARGET_DIR/$H/
                        chown -R $U.$U $TARGET_DIR/$H/test
                        chmod -R u+w $TARGET_DIR/$H/test
                        ##su - -c " $HOME_DIR/$CLASS_DIR/$GIT_DIR ; git config pull.rebase false"
                        ##su - $U -c "cd $HOME_DIR/$CLASS_DIR/$GIT_DIR ; git stash; git pull"
                        ##su - $U -c "cd $HOME_DIR/$CLASS_DIR/$GIT_DIR ; git pull"
                done
        fi
done
echo "Done."
