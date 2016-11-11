#!/bin/bash

# $USER should be defined as the user's loginname, and $PWD as the current directory
OUTPUT=/user/$USER/output/dt_configs_evaluation_$1
hdfs dfs -rm -r -f -skipTrash $OUTPUT

yarn \
    jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming-2.7.1.2.4.2.0-258.jar \
    -D mapred.reduce.tasks=0 \
    -D mapred.min.split.size=32 \
    -mapper "$PWD/mapper.py" \
    -input "/user/$USER/data/dt_configs/*" \
    -output $OUTPUT
