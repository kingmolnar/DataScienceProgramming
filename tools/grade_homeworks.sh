#!/bin/bash
cat <<'EOF'
 ██████╗ ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗     ██╗  ██╗██╗    ██╗
██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝     ██║  ██║██║    ██║
██║  ███╗██████╔╝███████║██║  ██║██║██╔██╗ ██║██║  ███╗    ███████║██║ █╗ ██║
██║   ██║██╔══██╗██╔══██║██║  ██║██║██║╚██╗██║██║   ██║    ██╔══██║██║███╗██║
╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝    ██║  ██║╚███╔███╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═╝ ╚══╝╚══╝ 
                                                                             
EOF
ASSIGNMENT=$1
if [ -z "$ASSIGNMENT"]
then
    echo "Usage: `basename $0` HWnn"
    echo "        with nn in [01, 02, ..., 08]"
    exit
fi

MAIN_DIR="`dirname $0`/.."
CLASS_DIR=IFI8410F23
GIT_REPO=https://github.com/kingmolnar/DataScienceProgramming.git
GIT_DIR=DataScienceProgramming

declare -A TEST_DIR
TEST_DIR["HW01"]="${MAIN_DIR}/01-Intro-UNIX/HW01/test"
TEST_DIR["HW02"]="${MAIN_DIR}/Homework/HW02/test"
TEST_DIR["HW03"]="${MAIN_DIR}/Homework/HW03/test"
TEST_DIR["HW04"]="${MAIN_DIR}/Homework/HW04/test"
TEST_DIR["HW05"]="${MAIN_DIR}/Homework/HW05/test"

BACKUP_DIR="${MAIN_DIR}/private/backup"
LOG_DIR="${MAIN_DIR}/log"
DSTAMP=`date +"%Y%m%d_%H%M%S"`

T_DIR=`realpath ${TEST_DIR[$ASSIGNMENT]}`
PYTEST_OPTS="--setup-timeout 10 --execution-timeout 120 --teardown-timeout 10"

echo "--------------------------------------------------------------------------------"
echo "Test: ${T_DIR}"
echo "--------------------------------------------------------------------------------"
cat $MAIN_DIR/private/ifi8410_users.log | while read U S D
do
        echo $U
        HOME_DIR="${BACKUP_DIR}/${U}"
       
        if [ -d ${HOME_DIR}/${ASSIGNMENT} ]
        then
            printf "${ASSIGNMENT}\t$U\tTEST START\n"
            bash -c "cd ${HOME_DIR}/${ASSIGNMENT}; python3 -m pytest ${T_DIR}" 2>&1 \
                | awk "{print \"$ASSIGNMENT\t$U\t\", \$0}" \
                | tee -ai "${LOG_DIR}/grades_${ASSIGNMENT}_${DSTAMP}.log"
            printf "${ASSIGNMENT}\t$U\tTEST END\n\n"
        else
            printf "$ASSIGNMENT\t$U\tNO ASSIGNMENT\n\n"
        fi
done
echo "Done."
