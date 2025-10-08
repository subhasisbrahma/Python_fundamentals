"""Demonstrates the use of the Ternary Conditional Operator (a one-line if/else
statement) to concisely assign a value based on a condition."""

first_number = 10
second_number = 20

# Ternary Conditional Operator Syntax:
# [value_if_true] if [condition] else [value_if_false]

# This line checks: Is first_number (10) less than second_number (20)?
# If True, assign 'first_number' (10) to 'smaller_number'.
# If False, assign 'second_number' (20) to 'smaller_number'.
smaller_number = first_number if first_number < second_number else second_number

print(f"First Number: {first_number}")
print(f"Second Number: {second_number}")
print(f"The smaller number is: {smaller_number}")  # Output: The smaller number is: 10
