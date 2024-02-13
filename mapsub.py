#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    entry = line.split(",")
    matrix_key = entry[0]
    row_index = int(entry[1])
    col_index = int(entry[2])
    value = int(entry[3])

    print(f'{row_index},{col_index},{matrix_key},{value}')

