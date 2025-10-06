"""Add a user-specified number of values and display the total sum."""

# Get the upper limit (N) from the user.
limit_number = int(input("Enter the number: "))

# Initialize the accumulator variable.
current_sum = 0

# The loop must run up to and including 'limit_number'.
# Therefore, we use range(limit_number + 1) which generates numbers from 0 up to N.
for current_number in range(limit_number + 1):
    
    # Add the current number in the sequence to the running total.
    current_sum = current_sum + current_number

# Print the final result after the loop completes.
print(current_sum)
# Example Output for N=5: 15 (since 0+1+2+3+4+5 = 15)

# Note on Efficiency:
# The mathematical formula for this calculation is N * (N + 1) / 2.
# For example, sum = limit_number * (limit_number + 1) // 2
# Using the formula is much faster for very large numbers than iterating with a loop.