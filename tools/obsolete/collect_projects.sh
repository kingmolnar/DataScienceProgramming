#!/bin/bash
cat << 'EOF'
 ██████╗ ██████╗ ██╗     ██╗     ███████╗ ██████╗████████╗                     
██╔════╝██╔═══██╗██║     ██║     ██╔════╝██╔════╝╚══██╔══╝                     
██║     ██║   ██║██║     ██║     █████╗  ██║        ██║                        
██║     ██║   ██║██║     ██║     ██╔══╝  ██║        ██║                        
╚██████╗╚██████╔╝███████╗███████╗███████╗╚██████╗   ██║                        
 ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝                        
                                                                               
██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗███████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   ███████╗
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   ╚════██║
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   ███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝
                                                                  
EOF
if [ $UID != 0 ]
then
    echo
    echo "Run this command with 'sudo' or  as root"
    exit
fi

MAIN_DIR="`dirname $0`/.."
CLASS_DIR=IFI8410F24
GIT_REPO=https://github.com/kingmolnar/DataScienceProgramming.git
GIT_DIR=DataScienceProgramming
# GIT_DIR=DataScienceProgramming/Homework
PROJECT_1=DataExplorationProject
PROJECT_2=MachineLearningProject
BACKUP_DIR=$MAIN_DIR/private/backup


TS=`date +"%Y%m%d_%H%M"`


function process_user() {
    U=$1
    echo $U
    HOME_DIR=/home/$U
    # mkdir -p $BACKUP_DIR/$HOMEWORK/$U/$TS 
    # mkdir -p $BACKUP_DIR/$U/$TS 
    mkdir -p $BACKUP_DIR/$U
    for PRJ in $PROJECT_1 $PROJECT_2
    do
        if [ -d "$HOME_DIR/$CLASS_DIR/$GIT_DIR/$PRJ" ]
        then
            printf "$TS\t$U\SUBMISSION START\n"
            cp -av $HOME_DIR/$CLASS_DIR/$GIT_DIR/$PRJ $BACKUP_DIR/$U/ | awk "{print \"$TS\t$U\t\", \$0}"
            date > $BACKUP_DIR/$U/SUBMISSION
            printf "$TS\t$U\SUBMISSION END\n\n"
        else
            date > $BACKUP_DIR/$U/$TS/NO_SUBMISSION
            printf "$HOME_DIR/$CLASS_DIR/$GIT_DIR/$TS\t$U\tNO SUBMISSION\n\n"
        fi
    done
    return
}

if [ -z "$1" ]
then
    cat $MAIN_DIR/private/ifi8410_users.log | while read USR S D
    do
        process_user $USR
    done
else
    process_user $1
fi

echo "Updating permissions. Please wait..."
chown -R pmolnar.pmolnar $BACKUP_DIR

echo "Done."


