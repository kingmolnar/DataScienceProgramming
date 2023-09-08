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

MAIN_DIR="`dirname $0`/.."
CLASS_DIR=IFI8410F23
GIT_REPO=https://github.com/kingmolnar/DataScienceProgramming.git
GIT_DIR=DataScienceProgramming
ASSIGNMENT="01-Intro-UNIX/HW01"
BACKUP_DIR=$MAIN_DIR/private/backup

HOMEWORK=`basename $ASSIGNMENT`



cat $MAIN_DIR/private/ifi8410_users.log | while read U S D
do
        echo $U
        HOME_DIR=/home/$U
        mkdir -p $BACKUP_DIR/$HOMEWORK/$U 
        if [ -d $HOME_DIR/$CLASS_DIR/$GIT_DIR/$ASSIGNMENT ]
        then
            printf "$ASSIGNMENT\t$U\SUBMISSION START\n"
            cp -av $HOME_DIR/$CLASS_DIR/$GIT_DIR/$ASSIGNMENT $BACKUP_DIR/$HOMEWORK/$U/ | awk "{print \"$ASSIGNMENT\t$U\t\", \$0}"
            date > $BACKUP_DIR/$HOMEWORK/$U/SUBMISSION
            printf "$ASSIGNMENT\t$U\SUBMISSION END\n\n"
            #printf "$ASSIGNMENT\t$U\tTEST START\n"
            #su - $U -c "cd $HOME_DIR/$CLASS_DIR/$GIT_DIR/$ASSIGNMENT; pytest" 2>&1 | awk "{print \"$ASSIGNMENT\t$U\t\", \$0}"
            #printf "$ASSIGNMENT\t$U\tTEST END\n\n"
        else
            date > $BACKUP_DIR/$HOMEWORK/$U/NO_SUBMISSION
            printf "$HOME_DIR/$CLASS_DIR/$GIT_DIR/$ASSIGNMENT\t$U\tNO SUBMISSION\n\n"
        fi
done

chown -R pmolnar.pmolnar $BACKUP_DIR

echo "Done."


