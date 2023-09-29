#!/bin/bash
cat << 'EOF'
 ██████╗ ██████╗ ██╗     ██╗     ███████╗ ██████╗████████╗                     
██╔════╝██╔═══██╗██║     ██║     ██╔════╝██╔════╝╚══██╔══╝                     
██║     ██║   ██║██║     ██║     █████╗  ██║        ██║                        
██║     ██║   ██║██║     ██║     ██╔══╝  ██║        ██║                        
╚██████╗╚██████╔╝███████╗███████╗███████╗╚██████╗   ██║                        
 ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝                        
                                                                               
██╗  ██╗ ██████╗ ███╗   ███╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗███████╗
██║  ██║██╔═══██╗████╗ ████║██╔════╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝
███████║██║   ██║██╔████╔██║█████╗  ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ███████╗
██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  ██║███╗██║██║   ██║██╔══██╗██╔═██╗ ╚════██║
██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗███████║
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
EOF
if [ $UID != 0 ]
then
    echo
    echo "Run this command with 'sudo' or  as root"
    exit
fi

MAIN_DIR="`dirname $0`/.."
CLASS_DIR=IFI8410F23
GIT_REPO=https://github.com/kingmolnar/DataScienceProgramming.git
GIT_DIR=DataScienceProgramming
BACKUP_DIR=$MAIN_DIR/private/backup


TS=`date +"%Y%m%d_%H%M"`

cat $MAIN_DIR/private/ifi8410_users.log | while read U S D
do
        echo $U
        HOME_DIR=/home/$U
        mkdir -p $BACKUP_DIR/$HOMEWORK/$U/$TS 
        if [ -d "$HOME_DIR/$CLASS_DIR/$GIT_DIR" ]
        then
            printf "$TS\t$U\SUBMISSION START\n"
            cp -av $HOME_DIR/$CLASS_DIR/$GIT_DIR $BACKUP_DIR/$U/$TS | awk "{print \"$TS\t$U\t\", \$0}"
            date > $BACKUP_DIR/$U/SUBMISSION
            printf "$TS\t$U\SUBMISSION END\n\n"
        else
            date > $BACKUP_DIR/$U/$TS/NO_SUBMISSION
            printf "$HOME_DIR/$CLASS_DIR/$GIT_DIR/$TS\t$U\tNO SUBMISSION\n\n"
        fi
done

chown -R pmolnar.pmolnar $BACKUP_DIR

echo "Done."


