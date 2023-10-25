#!/bin/bash
if [ $# -lt 2 ]; then
	echo "Usage `basename $0` INPUTFILE OUTPUTFILE"
	exit
fi
INP=$1
OUT=$2
echo `head -1 < $INP | tr -d '()' | tr ' ' '_' ` >$OUT
cat $INP | tail -n +3 | cut -d';' -f2- | cat -b |  tr '\t' ';' | tr -d ' '>> $OUT

