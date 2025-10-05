"""Shows how to declare variables and use basic arithmetic operators in Python."""

# Use clear, descriptive names (snake_case) for variables.
current_value = 10
print("Initial value:", current_value)  # Output: Initial value: 10

# Reassigning the variable: The new value (10 + 1) overwrites the old one.
current_value = current_value + 1
print("Value after increment:", current_value)  # Output: Value after increment: 11



# Getting User Input
# Prompt the user for input and immediately convert it to an integer using int().
# Without int(), the input would be stored as a string.
print("Please enter any whole number:")
user_input_number = int(input())

# The value entered by the user is now stored in the variable.
print("You entered:", user_input_number)
# Example Output if user types '45': You entered: 45



# Variable Deletion (The 'del' keyword)
variable_to_delete = 100
print("Before deletion:", variable_to_delete)  # Output: Before deletion: 100

# The 'del' keyword removes the variable name from Python's memory.
del variable_to_delete


# Shorthand Operators
# The '+=' operator is shorthand for 'count = count + 1' (addition assignment)
count = 7
count += 1
print("Count after += 1:", count)  # Output: Count after += 1: 8

# The '-=' operator is shorthand for 'count = count - 1' (subtraction assignment)
count = 8
count -= 1
print("Count after -= 1:", count)  # Output: Count after -= 1: 7


# The 'in' operator checks if a sequence (like a substring or item) is present
# within another sequence. It returns a boolean value (True or False).

print("Subhasis" in "Subhasis Brahma")  # Output: True

print("XYZ" in "Subhasis Brahma")  # Output: False
