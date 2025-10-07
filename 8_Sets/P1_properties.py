"""Introduces set properties in Python."""

# 1. Creation and Uniqueness

# Sets are defined using curly braces {}. Duplicate values are automatically removed.
initial_elements = {1, 2, 3, 4, 5, 5, 4}
print("--- 1. Uniqueness (No Duplicates) ---")
print(f"Set after removing duplicates: {initial_elements}") # Output: {1, 2, 3, 4, 5}

# Sets do not have a specific, guaranteed order.
print("Note: Output order may vary across Python runs.")


# 2. Lack of Indexing (Mutability Test)


# A set is mutable: you can add or remove elements.
print(f"Set before add: {initial_elements}")
initial_elements.add(6)
print(f"Set after add(6): {initial_elements}") # The set object is changed in place.

# We CANNOT access elements by index because sets are unordered.
# Uncommenting the following line will raise TypeError
# print(initial_elements[0])


# 3. Element Immutability Requirement


# Immutable elements (like int, float, str, tuple) are allowed.
hashable_set = {1, "text", (1, 2)}
print(f"Set with valid immutable elements: {hashable_set}")

# Mutable elements (like lists, dictionaries, or other sets) are NOT allowed.
# Uncommenting the following line will raise TypeError
# unhashable_set = {1, [2, 3]}
