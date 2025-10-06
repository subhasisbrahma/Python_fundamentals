"""Print the multiplication table of a given number using loops."""

# Get the base number for the table from the user.
base_number = int(input("Enter the number: "))

print()

# Generate and print the multiplication table
for multiplier in range(1, 11):
    product = base_number * multiplier
    print(base_number, "X", multiplier, "=", product)
    # Example Output for base_number=7: 7 X 1 = 7, 7 X 2 = 14, etc.
