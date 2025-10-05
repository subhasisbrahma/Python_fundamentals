"""Explores different types of Python operators: arithmetic, comparison, logical, and assignment."""

# Arithmetic Operators
# Used for mathematical calculations.
# Key operators: +, -, *, /, // (floor division), % (modulus/remainder), ** (power).

example_division = 10 / 3    # Standard division (float result)
example_floor_division = 10 // 3 # Floor Division (gives only the integer part, result is 3)
example_remainder = 10 % 3   # Modulus (gives the remainder, result is 1)
example_power = 2 ** 3       # Power (2 raised to the power of 3, result is 8)

print("10 / 3 =",example_division)      # Output: 10 / 3 = 3.3333333333333335
print("10 // 3 =",example_floor_division)# Output: 10 // 3 = 3
print("10 % 3 =",example_remainder)     # Output: 10 % 3 = 1
print("2 ** 3 =",example_power)         # Output: 2 ** 3 = 8


# Relational (Comparison) Operators
# These operators compare two values and always return a boolean (True or False).
# Key operators: >, <, >=, <=, == (equal to), != (not equal to).

is_equal = (5 == 5)        # True
is_greater = (10 > 20)     # False
is_not_equal = (5 != 6)    # True

print("Is 5 equal to 5?", is_equal)      # Output: Is 5 equal to 5? True
print("Is 10 greater than 20?", is_greater)# Output: Is 10 greater than 20? False


# Logical Operators
# Used to combine or modify boolean values (True/False).
# Key operators: and, or, not.

print(True and True)    # Output: True
print(True and False)   # Output: False
print(False and True)   # Output: False
print(False and False)  # Output: False

print(True or True)     # Output: True
print(True or False)    # Output: True
print(False or True)    # Output: True
print(False or False)   # Output: False

print(not(True))        # Output: False
print(not(False))       # Output: True