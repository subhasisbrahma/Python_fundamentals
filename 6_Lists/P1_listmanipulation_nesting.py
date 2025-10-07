""" Demonstrates list manipulation techniques and nested list structures."""

# 1. List Manipulation (append and remove)

# Initialize a list of integers.
my_list = [7, 8, 15, 22, 1, 9]
print("Initial List:", my_list)

# append(): Adds the new element to the end of the list.
my_list.append(11)
print("After appending 11:", my_list)

# Lists allow duplicate values, unlike sets.
my_list.append(8)
print("After appending duplicate 8:", my_list)

# remove(): Finds the first occurrence of the value and removes it.
# The duplicate 8 remains in the list.
my_list.remove(8)
print("After removing first '8':", my_list)

# Note: If the value is not found, list.remove() will raise a ValueError.


# 2. Nested List Structures

# L1: An inner list initialized.
inner_list_one = []
inner_list_one.append(1)
inner_list_one.append(2)
inner_list_one.append(3)
print("Inner List One:", inner_list_one)  # Output: [1, 2, 3]

# L2: A list (the container) initialized.
container_list = []
container_list.append(inner_list_one)
print("Container after adding L1:", container_list)  # Output: [[1, 2, 3]]

# L3: A second list to be added.
inner_list_two = [4, 5, 6]
container_list.append(inner_list_two)
print("Container after adding L2:", container_list)  # Output: [[1, 2, 3], [4, 5, 6]]

# L4: Nesting the container_list inside a new top-level list.
top_level_list = []
top_level_list.append(container_list)
top_level_list.append([10, 20, 30])

print("Final Nested List (T):", top_level_list)
# Output: [[[1, 2, 3], [4, 5, 6]], [10, 20, 30]]

# Accessing Elements in the Nested Structure:

# Access the 0th element, which is the list: [[1, 2, 3], [4, 5, 6]]
print("Element t[0] (a list of lists):", top_level_list[0])

# Access the 1st element, which is the list: [10, 20, 30]
print("Element t[1] (a list):", top_level_list[1])

# Accessing the element '1' from the structure:
# top_level_list[0] -> [[1, 2, 3], [4, 5, 6]]
# [0] again -> [1, 2, 3]
# [0] again -> 1
print("Accessing '1' from T[0][0][0]:", top_level_list[0][0][0])
