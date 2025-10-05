"""Shows how to concatenate strings and mix text with variables in print statements."""

# String Concatenation

first_name = "Subhasis"
last_name = "Brahma"

# The '+' operator joins two strings end-to-end.
# Note: There is no automatic space added, so the result is "SubhasisBrahma".
full_name = first_name + last_name
print("Concatenated string:", full_name)  # Output: Concatenated string: SubhasisBrahma

# To add a space: full_name = first_name + " " + last_name


# List Concatenation

list_of_numbers_a = [1, 2, 3, 4]
list_of_numbers_b = [5, 6, 7]

# The '+' operator creates a new list containing all elements from both lists,
# preserving the order.
combined_list = list_of_numbers_a + list_of_numbers_b

print("Concatenated list:", combined_list)  # Output: Concatenated list: [1, 2, 3, 4, 5, 6, 7]
