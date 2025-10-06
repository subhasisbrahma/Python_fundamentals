"""Check whether a given number or string is a palindrome."""

# Get the number to be checked.
input_number = int(input("Enter the number: "))

# 1. Prepare for Reversal
# We take the absolute value so the reversal logic only deals with positive digits.
absolute_number = abs(input_number)
reversed_number = 0

# 2. Reversal Loop
# This loop mathematically reconstructs the number in reverse order.
while (absolute_number > 0):
    # Get the last digit (remainder)
    remainder = absolute_number % 10
    
    # Build the reversed number: shift existing digits left and add the remainder
    reversed_number = reversed_number * 10 + remainder
    
    # Remove the last digit using floor division
    absolute_number = absolute_number // 10

# 3. Restore the Sign
# If the original number was negative, the reversed result must also be negative
# to allow for a direct comparison with the original number.
if (input_number < 0):
    reversed_number = -reversed_number

# 4. Palindrome Check
# Compare the original input number with the fully reversed, signed number.
if (input_number == reversed_number):
    print("Palindrome")
    # Example Output for 121 or -121: Palindrome
else:
    print("Not a Palindrome")
    # Example Output for 123 or -123: Not a Palindrome