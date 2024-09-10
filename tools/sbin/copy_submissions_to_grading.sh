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

find  ${SUBMISSIONS_DIR}/${TERM}/ -type d -name "${HW}" | while read SOURCE REST
do
    echo "Processing ${SOURCE}"
    TARGET=`echo ${SOURCE} | sed "s|${SUBMISSIONS_DIR}|${GRADING_DIR}|"`
    echo "Copying to ${TARGET}"
done


