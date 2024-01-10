#!/bin/bash
tr -d '.,:?"' \
| tr 'A-Z' 'a-z' \
| tr ' ' '\n' \
| grep -v -e '^[[:space:]]*$' \
| sort \
| uniq -c \
| sort -rn

