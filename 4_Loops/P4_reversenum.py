"""Reverse the digits of a given integer."""

# Get the number from the user
input_number = int(input("Enter the number to reverse (e.g., 123 or -456): "))

# --- Method 1: Pre-seed Logic ---

absolute_number = abs(input_number)
reversed_number = absolute_number % 10
absolute_number = absolute_number // 10

while absolute_number > 0:
    remainder = absolute_number % 10
    reversed_number = reversed_number * 10 + remainder
    absolute_number = absolute_number // 10

if input_number < 0:
    reversed_number = -reversed_number

print("Input:", input_number, ", Reversed:", reversed_number)


# --- Method 2: Standard Logic ---
print()

absolute_number = abs(input_number)
reversed_number = 0

while absolute_number > 0:
    remainder = absolute_number % 10
    reversed_number = reversed_number * 10 + remainder
    absolute_number = absolute_number // 10

if input_number < 0:
    reversed_number = -reversed_number

print("Input:", input_number, ", Reversed:", reversed_number)
