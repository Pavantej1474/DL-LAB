#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    matrix, row, col, value = line.split(',')
    
    if matrix == 'a':
        for k in range(3):  # Assuming a 3x3 matrix
            print(f'{row},{col},{k},{value},a')
    elif matrix == 'b':
        for k in range(3):  # Assuming a 3x3 matrix
            print(f'{k},{col},{row},{value},b')

