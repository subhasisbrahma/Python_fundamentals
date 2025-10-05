"""Demonstrates Python's dynamic typing feature"""

# 1. Initial Assignment
initial_number = 8
print("Initial value:", initial_number, ", Type:", type(initial_number))
# Output: Initial value: 8, Type: <class 'int'>

# 2. Standard Division (Type Promotion)
# The '/' operator is used for true division. Since the result of any true
# division *could* be a decimal, Python ensures accuracy by promoting the
# result to a 'float' type.
initial_number = initial_number / 2
# The variable now holds the value 4.0, not 4.

print("Value after division:", initial_number, ", Type:", type(initial_number))
# Output: Value after division: 4.0, Type: <class 'float'>

# Note: If you want to keep the result as an integer, you must use
# Floor Division (//):
# example = 8 // 2  # Result is 4, type is <class 'int'>
