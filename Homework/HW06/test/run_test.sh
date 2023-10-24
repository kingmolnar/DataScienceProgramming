#!/bin/bash

TEST_DIR=`dirname $0`
WORK_DIR=`dirname $TEST_DIR`

pushd $WORK_DIR
for T in $TEST_DIR/*.py
do
	python3 -m pytest $T
done
popd

