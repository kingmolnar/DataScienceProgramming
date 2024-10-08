#!/bin/bash
cat <<'EOF'
  ____        _               _         _                 
 / ___| _   _| |__  _ __ ___ (_)___ ___(_) ___  _ __  ___ 
 \___ \| | | | '_ \| '_ ` _ \| / __/ __| |/ _ \| '_ \/ __|
  ___) | |_| | |_) | | | | | | \__ \__ \ | (_) | | | \__ \
 |____/ \__,_|_.__/|_| |_| |_|_|___/___/_|\___/|_| |_|___/
      __     ____               _ _                       
  ____\ \   / ___|_ __ __ _  __| (_)_ __   __ _           
 |_____\ \ | |  _| '__/ _` |/ _` | | '_ \ / _` |          
 |_____/ / | |_| | | | (_| | (_| | | | | | (_| |          
      /_/   \____|_|  \__,_|\__,_|_|_| |_|\__, |          
                                          |___/           
EOF

TERM="F24"
USER_ID="mjack6"
GROUP_ID="mjack6"
SUBMISSIONS_DIR="/data/IFI8410_submissions"
GRADING_DIR="/data/IFI8410_grading"
MAIN_DIR="`dirname $0`/../.."

## check is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

if [ -z "$1" ]; then
    echo "Usage: `basename $0` HWnn"
    exit 1
fi

HW="$1"

mkdir -p ${GRADING_DIR}/${TERM}/
chmod -R o-rwx ${GRADING_DIR}
chown -R ${USER_ID}.${GROUP_ID} ${GRADING_DIR}

find  ${SUBMISSIONS_DIR}/${TERM}/ -type d -name "${HW}" | while read SOURCE REST
do
    TS=`date +"%Y-%m-%d %H:%M:%S"`
    echo "$HW --- $TS --- Processing ${SOURCE}"
    TARGET=`echo ${SOURCE} | sed "s|${SUBMISSIONS_DIR}|${GRADING_DIR}|"`
    echo "$HW --- $TS --- Copying to ${TARGET}"
    mkdir -p ${TARGET}
    cp -r ${SOURCE}/* ${TARGET}/ || echo "$HW --- $TS --- ERROR --- Failed to copy from ${SOURCE} to ${TARGET}"
    chown -R ${USER_ID}.${GROUP_ID} ${TARGET} || echo "$HW --- $TS --- ERROR --- Failed to change ownership of ${TARGET}"
    chmod -R o-rwx ${TARGET} || echo "$HW --- $TS --- ERROR --- Failed to set permissions of ${TARGET}"
done


