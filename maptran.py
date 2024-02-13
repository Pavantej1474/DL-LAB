#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    matrix, row, col, value = line.split(',')
    print(f'{col},{row},{value},{matrix}')

