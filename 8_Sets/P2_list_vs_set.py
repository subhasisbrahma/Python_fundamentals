"""Compares sets and lists."""

import sys

# 1. Search Efficiency (Membership Check: 'in')

# Concept: Sets are much faster for membership checks because they use
# a hash table (O(1) complexity, or constant time). Lists require a linear
# scan (O(n) complexity, or time scales with size).

small_list = [10, 20, 30, 40]
small_set = {10, 20, 30, 40}

print("List Check (-1 in list): This is slow for very large lists.")
print(-1 in small_list) # Output: False

print("Set Check (-1 in set): This is extremely fast, regardless of size.")
print(-1 in small_set)  # Output: False


# 2. Memory Overhead

# Sets require more memory than lists because they must store hash values
# for every element to enable their fast lookup speed.

# Create containers with 100 elements for comparison.
list_for_size = list(range(100))
set_for_size = set(range(100))

list_size = sys.getsizeof(list_for_size)
set_size = sys.getsizeof(set_for_size)

print(f"List Size (100 elements): {list_size} bytes")
print(f"Set Size (100 elements): {set_size} bytes")

if set_size > list_size:
    print("Observation: The Set is larger due to hash table overhead.")


# 3. Indexing Capability

# Lists are ordered and support indexing. Sets are UNORDERED and do not support indexing.
print(f"List index 0: {list_for_size[0]}") # Output: 0 (Successful)

# Accessing a set by index will fail. Uncommenting the following line will raise TypeError.
# print(set_for_size[0])
print("Set Indexing Error: Cannot access set elements by index.")
print("Conclusion: Sets are UNORDERED and cannot be accessed by index.")

