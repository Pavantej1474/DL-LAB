#!/usr/bin/python
import sys

# Initialize a dictionary to store intermediate results
result = {}

# Iterate over each input line from the mapper
for input_line in sys.stdin:
    # Remove leading and trailing whitespaces
    input_line = input_line.strip()

    # Split the input line into components
    row_index, col_index, matrix_key, value = input_line.split(',')

    # Skip non-numeric values
    if not value.isdigit():
        continue

    # Initialize result dictionary if the key does not exist
    if (row_index, col_index) not in result:
        result[(row_index, col_index)] = {'a': 0, 'b': 0}

    # Accumulate values for matrix subtraction
    if matrix_key == 'a':
        result[(row_index, col_index)]['a'] = int(value)
    elif matrix_key == 'b':
        result[(row_index, col_index)]['b'] = int(value)

# Output the result as a matrix
for i in range(3):  # Assuming a 3x3 matrix
    for j in range(3):
        result_value = result[(str(i), str(j))]['a'] + result[(str(i), str(j))]['b']
        print(result_value, end=' ')
    print()

