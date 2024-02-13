#!/user/bin/python3
import sys
# Function to perform Matrix Multiplication
def multiply_reducer(key, values):
   a_values = []
   b_values = []
   for value in values:
       matrix, indices, data = value.split('\t')
       indices = indices.split(',')
       data = int(data)
       if matrix == 'a_multiply':
           a_values.append((indices[1], data))
       elif matrix == 'b_multiply':
           b_values.append((indices[1], data))
   result = 0
   for i, a_val in a_values:
       for j, b_val in b_values:
           if i == j:
               result += a_val * b_val
   emit(key, result)
# Function to emit key-value pairs
def emit(key, value):
   print(f"{key}\t{value}")
# Read input from stdin
current_key = None
current_values = []
for line in sys.stdin:
   line = line.strip()
   key, value = line.split('\t', 1)
   if current_key == key:
       current_values.append(value)
   else:
       if current_key:
           multiply_reducer(current_key, current_values)
       current_key = key
       current_values = [value]
# Process the last key-value pair
if current_key:
   multiply_reducer(current_key, current_values)
	
