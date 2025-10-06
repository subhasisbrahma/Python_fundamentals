"""Check if a number ends with digit 0 or 5 (useful for divisibility by 5 or 10)."""

# Get input from the user and convert it to an integer.
input_number = int(input("Enter a number: "))

# Outer Condition: Check if the number is divisible by 5 (remainder is 0).
if (input_number % 5 == 0):
    # Inner Condition: If divisible by 5, check if it's ALSO divisible by 10.
    if (input_number % 10 == 0):
        # If divisible by both 5 and 10 (e.g., 10, 20, 100)
        print("0")
        # Example Output if user enters '50': 0
    else:
        # If divisible by 5 BUT NOT 10 (meaning it must end in 5, e.g., 5, 15, 25)
        print("5")
        # Example Output if user enters '15': 5
else:
    # Final Condition: The number is not divisible by 5 (e.g., 1, 2, 7)
    print("other")
    # Example Output if user enters '7': other