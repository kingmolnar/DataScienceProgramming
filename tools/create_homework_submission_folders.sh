#!/bin/bash
cat <<'EOF'
  _   _                                         _     
 | | | | ___  _ __ ___   _____      _____  _ __| | __ 
 | |_| |/ _ \| '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ / 
 |  _  | (_) | | | | | |  __/\ V  V / (_) | |  |   <  
 |_|_|_|\___/|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\ 
 / ___| _   _| |__  _ __ ___ (_)___ ___(_) ___  _ __  
 \___ \| | | | '_ \| '_ ` _ \| / __/ __| |/ _ \| '_ \ 
  ___) | |_| | |_) | | | | | | \__ \__ \ | (_) | | | |
 |____/ \__,_|_.__/|_| |_| |_|_|___/___/_|\___/|_| |_|
 |  ___|__ | | __| | ___ _ __ ___                     
 | |_ / _ \| |/ _` |/ _ \ '__/ __|                    
 |  _| (_) | | (_| |  __/ |  \__ \                    
 |_|  \___/|_|\__,_|\___|_|  |___/    

EOF
TOOLS=`dirname $0`
DEST_DIR="/data/IFI8410_submissions"
TERM_DIR="F24"

if [ ! -d $DEST_DIR ]
then
    echo "Folder does not exist: $DEST_DIR"
    exit 1
fi

mkdir -p $DEST_DIR/$TERM_DIR
chmod o=x $DEST_DIR/$TERM_DIR

for STUDENT in `$TOOLS/students_list.py --with-ta` 
do
    echo "Student: $STUDENT"
    STUDENT_DIR="$DEST_DIR/$TERM_DIR/$STUDENT"
    if [ ! -d $STUDENT_DIR ]
    then
       mkdir -p $STUDENT_DIR
       for H in {00..10}
       do
           HW_DIR="${STUDENT_DIR}/HW${H}"
           mkdir -p $HW_DIR
       done
       sudo chgrp -R $STUDENT $STUDENT_DIR
       chmod -R o-rwx $STUDENT_DIR
       chmod -R g+w $STUDENT_DIR
       sudo chmod -R g+s $STUDENT_DIR
    else
       echo "${STUDENT_DIR} already exists."
    fi
done
# ls -lR $DEST_DIR/$TERM_DIR
echo "Done."
