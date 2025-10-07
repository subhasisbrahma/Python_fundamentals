"""Explains list mutability."""

data_list = [1, 2, 4]
print("--- List (MUTABLE) Demonstration ---")
print(f"Initial List: {data_list}")  # Output: [1, 2, 4]

# Access the element at index 2 and directly assign a new value (3).
# The list object itself is changed.
data_list[2] = 3
print(f"List after changing index 2 to 3: {data_list}")  # Output: [1, 2, 3]


# String: IMMUTABLE (Cannot be modified in place)


data_string = "subhasis"
print(f"Initial String: {data_string}")  # Output: subhasis

# We can access a character using indexing, but we cannot modify it.
print(f"Character at index 3: {data_string[3]}")  # Output: h

# Instead of modifying, we create a NEW string to demonstrate the change
new_string = data_string[:3] + 'k' + data_string[4:]
print(f"New string after replacing index 3 with 'k': {new_string}")  # Output: subkasis

# Explanation for immutability:
print("Explanation: Strings are IMMUTABLE. You cannot change individual characters in place.")
print("To change a string, you must create a NEW string (e.g., using slicing or replace()).")
