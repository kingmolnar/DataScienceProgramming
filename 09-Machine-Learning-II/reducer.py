#!/usr/bin/python
import os
import sys
 
last_key = None
running_total = 0
 
for input_line in sys.stdin:
    input_line = input_line.strip()
    try:
        inp = input_line.split("\t")
        this_key = inp[0]
        value = int(inp[1])

        if last_key == this_key:
            running_total += value
        else:
            if last_key:
                print( "%s\t%d" % (last_key, running_total) )
            running_total = value
            last_key = this_key
    except:
        None
        
if last_key == this_key:
    print( "%s\t%d" % (last_key, running_total) )