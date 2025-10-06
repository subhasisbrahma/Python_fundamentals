"""Determine if numbers are odd or even within a given range using loops."""

# Get the upper bound for the range from the user.
limit_number = int(input("Enter a number: "))

# Iterate through numbers from 0 up to limit_number - 1
for current_number in range(limit_number):
    if current_number % 2 == 0:
        print(current_number, "is Even")
        # Example Output for 0, 2, 4...: 0 is Even
    else:
        print(current_number, "is Odd")
        # Example Output for 1, 3, 5...: 1 is Odd
