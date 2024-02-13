#!/usr/bin/python
import sys

result = {}

for input_line in sys.stdin:
    input_line = input_line.strip()
    row_index, col_index, matrix_key, value = input_line.split(',')
    if not value.isdigit():
        continue
    if (row_index, col_index) not in result:
        result[(row_index, col_index)] = {'a': 0, 'b': 0}
    if matrix_key == 'a':
        result[(row_index, col_index)]['a'] = int(value)
    elif matrix_key == 'b':
        result[(row_index, col_index)]['b'] = int(value)

for i in range(3):  # Assuming a 3x3 matrix
    for j in range(3):
        result_value = result[(str(i), str(j))]['a'] - result[(str(i), str(j))]['b']
        print(result_value, end=' ')
    print()
