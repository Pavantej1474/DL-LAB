#!/usr/bin/python
import sys

current_key = None
current_values = []

def emit_result(values):
    values = sorted(values, key=lambda x: int(x[1]))
    result = [str(value[2]) for value in values]
    print(','.join(result))

for line in sys.stdin:
    line = line.strip()
    col, row, value, matrix = line.split(',')
    value = int(value)

    key = col

    if current_key == key:
        current_values.append((col, row, value, matrix))
    else:
        if current_key:
            emit_result(current_values)

        current_key = key
        current_values = [(col, row, value, matrix)]

if current_key:
    emit_result(current_values)

