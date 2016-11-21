#!/usr/bin/env python
import atexit
import os
import platform
import sys

os.environ["SPARK_HOME"] = '/usr/hdp/2.4.2.0-258/spark'
spark_home = os.environ.get('SPARK_HOME', None)
if not spark_home:
    raise ValueError('SPARK_HOME environment variable is not set')

sys.path.insert(0, os.path.join(spark_home, 'python'))
sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.8.1-src.zip'))
execfile(os.path.join(spark_home, 'python/pyspark/shell.py'))


###sys.path.append('/usr/hdp/2.4.2.0-258/spark/python')

import py4j

import pyspark
from pyspark.context import SparkContext
from pyspark.sql import SQLContext, HiveContext
from pyspark.storagelevel import StorageLevel

import json

def extract_hash(tw):
    try:
        return json.loads(tw)['entities']['hashtags']
    except:
        return ()
    
tweets = sc.textFile("/user/molnar/data/election2012/cache-*.json.gz")
hashtags = tweets.flatMap(extract_hash).map(lambda x: (x['text'], 1))
topcounts = hashtags.reduceByKey(lambda a, b: a+b)

res = topcounts.map(lambda (a,b): (b, a)).sortByKey(0,1).take(20)

print '\n'.join(res)

