#!/usr/bin/bash
/usr/bin/spark-submit --master yarn-client --queue default \
    --num-executors 120 --executor-memory 1G --executor-cores 2 \
    --driver-memory 1G \
    top_hashtags.py


