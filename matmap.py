#!/user/bin/python3
import sys
# Function to emit key-value pairs
def emit(key, value):
   print(f"{key}\t{value}")
# Function to perform Matrix Multiplication
def multiply_mapper(line):
   matrix, i, j, val = line.split(',')
   if matrix == 'a':
       for k in range(3):
           emit(f"{i},{k}", f"a_multiply,{j},{val}")
   else:
       for k in range(3):
           emit(f"{k},{j}", f"b_multiply,{i},{val}")
# Read input from stdin
for line in sys.stdin:
   line = line.strip()
   # Perform Matrix Multiplication
   multiply_mapper(line)
		
