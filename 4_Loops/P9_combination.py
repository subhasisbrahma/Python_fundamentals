"""Calculate combinations (nCr) using loops or the math library."""

# Define the input strings
string_a = "VIBGYOR"
string_b = "VIBGYOR"

# Initialize a counter
combination_count = 0

# Get the length of the strings
string_length = len(string_a)

# Nested loops to generate all combinations
for index_a in range(string_length):
    for index_b in range(string_length):
        char_a = string_a[index_a]
        char_b = string_b[index_b]
        print("(", char_a, ",", char_b, ")")
        combination_count += 1

# Print the total number of combinations
print()
print("The total combinations are:", combination_count)  # Output: 49
