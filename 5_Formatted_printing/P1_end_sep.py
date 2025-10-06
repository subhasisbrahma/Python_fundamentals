"""Demonstrate how 'end' and 'sep' parameters work in the print() function."""

# 1. The 'end' Argument

# The 'end' argument specifies what to print after the last item is outputted.
# By default, end='\n' (a newline character). Changing it to ' ' keeps the output
# on the same line, separated by a space.

print("--- Demonstration of 'end' ---")
for number in range(10):
    # Prints the number followed by a space, instead of a newline.
    print(number, end=' ')
    
# Output: 0 1 2 3 4 5 6 7 8 9
print() # Use a final, empty print() to ensure the next output starts on a new line.


# 2. The 'sep' Argument

# The 'sep' argument (separator) specifies what character to insert between
# items when printing multiple items passed in a single print() call.
# By default, sep=' ' (a space).

print("\n--- Demonstration of 'sep' ---")

# Define variables for a date structure.
day = 17
month = 1
year = 2025

# First print statement uses 'end' to keep the cursor on the same line.
print("Today's date is:", end=' ')

# Second print statement uses 'sep' to separate the date components with a '/'.
print(day, month, year, sep='/')
# Output: Today's date is: 17/1/2025