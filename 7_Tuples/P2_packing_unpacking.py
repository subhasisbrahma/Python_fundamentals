"""Demonstrates tuple packing and unpacking."""

# 1. Explicit Tuple

explicit_tuple = (1, 2, 3)
print("1. Explicit Tuple:", explicit_tuple, type(explicit_tuple)) 
# Output: (1, 2, 3) <class 'tuple'>


# 2. Packing and Unpacking

# PACKING: Python groups the multiple values on the right-hand side
# into a single tuple object, which is then assigned to the variable 'packed_data'.
packed_data = 4, 5, 6 
print(f"2. Implicit Packing:", packed_data, type(packed_data))
# Output: (4, 5, 6) <class 'tuple'>

# UNPACKING: The elements of the tuple (right-hand side) are assigned
# sequentially to the variables on the left-hand side.
x, y, z = packed_data 
print(f"3. Unpacking (x, y, z): {x}, {y}, {z}")
# Output: 4, 5, 6

# 3. The Pythonic Variable Swap Trick

first_value = 5
second_value = 10

print(f"4. Swap Trick: Before swap -> x={first_value}, y={second_value}")

# This single line performs:
# 1. PACKING: (10, 5) is created on the right-hand side.
# 2. UNPACKING: The tuple (10, 5) is unpacked into (first_value, second_value).
first_value, second_value = second_value, first_value 

print(f"Swap Trick: After swap -> x={first_value}, y={second_value}")
# Output: After swap -> x=10, y=5


# 4. Single-Element Tuple Syntax

# WARNING: Parentheses are ignored when defining a single item.
not_a_tuple = (7) 
print(f"5. (7) is NOT a tuple:", not_a_tuple, type(not_a_tuple))
# Output: 7 <class 'int'>

# Correct Syntax: A trailing comma is REQUIRED to tell Python it is a tuple.
is_a_tuple = (7,) 
print(f"6. (7,) IS a tuple:", is_a_tuple, type(is_a_tuple))
# Output: (7,) <class 'tuple'>
