"""Illustrates common list operations."""

# Concatenation (Addition): The '+' operator joins two lists to create a new list.
list_a = [1, 2, 3]
list_b = [4, 5, 6]
combined_list = list_a + list_b
print(f"List A + List B: {combined_list}")  # Output: [1, 2, 3, 4, 5, 6]


# Replication (Multiplication): The '*' operator repeats a list N times.
repeated_list = [1, 2, 3] * 3
print(f"List [1, 2, 3] * 3: {repeated_list}")  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

list_one = [1, 2, 3]
list_two = [1, 2, 3]
list_three = [1, 2, 4]
list_four = [2, 1]

# Equality (==): Lists are equal only if they have the same elements in the same order.
print(f"List [1, 2, 3] == [1, 2, 3]: {list_one == list_two}")      # Output: True
print(f"List [1, 2, 3] == [1, 2, 4]: {list_one == list_three}")    # Output: False

# Comparison (<, >): Lists are compared element by element (lexicographical comparison).
# Comparison stops at the first pair of elements that are different.
print(f"List [1, 2, 3] < [1, 2, 4]: {list_two < list_three}")      # Output: True
print(f"List [1, 2] < [2, 1]: {[1, 2] < list_four}")              # Output: True
print(f"List [1] < [1, 2, 3]: {[1] < [1, 2, 3]}")                 # Output: True
print(f"List [2, 3] < [3]: {[2, 3] < [3]}")                       # Output: True
print(f"List [] > [1]: {[] > [1]}")                               # Output: False

# 'in' checks if an element is present within the list.
data_list = [1, 2, 3, 4, 5]
print(f"Is 4 in {data_list}?: {4 in data_list}")  # Output: True
print(f"Is 6 in {data_list}?: {6 in data_list}")  # Output: False


