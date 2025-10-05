"""Introduces Python string basics: indexing and simple manipulations."""

# String Indexing and Concatenation

digit_string = "0123456789"

# Indexing extracts characters as individual strings.
digit_seven = digit_string[7]
digit_eight = digit_string[8]

# The '+' operator on two strings performs CONCATENATION (joining them).
# Python treats '7' and '8' as characters, not numbers, so the result is "78".
concatenated_result = digit_seven + digit_eight

print("String Concatenation:", concatenated_result)  # Output: String Concatenation: 78


# String Indexing with Explicit Type Casting (Addition)

# Use the same digit string for comparison.
d = "0123456789"

# We use the int() function to explicitly convert the string characters
# into integer numbers BEFORE performing the addition.
digit_int_seven = int(d[7])
digit_int_eight = int(d[8])

# The '+' operator on two integers performs ARITHMETIC ADDITION.
# The result is the numerical sum: 7 + 8 = 15.
arithmetic_result = digit_int_seven + digit_int_eight

print("Arithmetic Addition:", arithmetic_result)  # Output: Arithmetic Addition: 15


# 3. Triple Quotes for Multi-Line Text and Comments

# Purpose 1: Creating a multi-line string variable.
# The variable will store all the newline characters and spacing exactly as typed.
multi_line_text = '''Subhasis
Brahma'''

print(multi_line_text)
# Output:
# Subhasis
# Brahma

# Purpose 2: Creating a multi-line comment.
# If the triple-quoted block is NOT assigned to a variable, it acts as a comment
# or documentation (like the docstring at the top of this file).
'''
This block is not assigned to a variable, so it is ignored by Python
and serves only as a multi-line comment or extended documentation.
It's great for explaining a large section of code.
'''