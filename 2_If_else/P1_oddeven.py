"""Determine whether a user-provided number is odd or even."""

# Get input from the user and ensure it is converted to an integer (int).
input_number = int(input("Enter a number: "))

# Conditional Logic: Check if the number is even or odd.
# The modulo operator (%) returns the remainder of a division.
# If a number divided by 2 has a remainder of 0, it is even.
if (input_number % 2 == 0):
    print("Even")
    # Example Output if user enters '10': Even
else:
    # Otherwise, the remainder is 1, and the number is odd.
    print("Odd")
    # Example Output if user enters '7': Odd