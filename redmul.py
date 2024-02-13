#!/usr/bin/python
import sys
from operator import itemgetter

prev_key = None
current_key = None
value_list = []

def emit_result(key, result):
    print(f'{key[0]},{key[1]},{result}')

for line in sys.stdin:
    line = line.strip()
    row, col, index, value, matrix = line.split(',')
    value = int(value)

    current_key = (row, col)

    if current_key == prev_key:
        value_list.append((index, value, matrix))
    else:
        if prev_key:
            value_list = sorted(value_list, key=itemgetter(0))
            i = 0
            result = 0
            while i < len(value_list) - 1:
                if value_list[i][0] == value_list[i + 1][0]:
                    result += value_list[i][1] * value_list[i + 1][1]
                    i += 2
                else:
                    i += 1
            emit_result(prev_key, result)

        prev_key = current_key
        value_list = [(index, value, matrix)]

if current_key == prev_key:
    value_list = sorted(value_list, key=itemgetter(0))
    i = 0
    result = 0
    while i < len(value_list) - 1:
        if value_list[i][0] == value_list[i + 1][0]:
            result += value_list[i][1] * value_list[i + 1][1]
            i += 2
        else:
            i += 1
    emit_result(prev_key, result)

