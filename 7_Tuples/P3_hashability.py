"""Explains tuple hashability."""

# 1. Mutability of Nested Objects

# The tuple itself is IMMUTABLE, but the element at index 0 is a list, which is MUTABLE.
data_tuple = ([1, 2], ['a', 'b'])
print(f"Initial Tuple: {data_tuple}") # Output: ([1, 2], ['a', 'b'])

# Attempting to reassign data_tuple[0] = [9, 9] would raise a TypeError.

# We can still modify the list object that the tuple holds a reference to.
# We are changing the internal state of the list at index 0.
data_tuple[0][1] = 3 
print(f"After modifying list element t[0][1]: {data_tuple}") 
# Output: ([1, 3], ['a', 'b'])
print("Conclusion: The object is mutable, even though the container (tuple) is immutable.")


# 2. Hashability Rule


# A hashable object must have a fixed value throughout its lifetime.
# Python uses the __hash__() method to generate a unique integer ID.

# Hashable Example (Immutable Contents)
# This tuple only contains integers, which are immutable.
hashable_tuple = (1, 2, 3) 
print(f"Tuple (1, 2, 3) is Hashable. Hash: {hash(hashable_tuple)}")
# This tuple CAN be used as a dictionary key.

# Unhashable Example (Mutable Contents)
# This tuple contains a LIST, which is mutable. Therefore, the tuple's
# contents are not fixed, and it is considered UNHASHABLE.
# Uncommenting the following line will raise a TypeError at runtime.
# unhashable_tuple = ([1, 2, 3],)
# print(hash(unhashable_tuple))
print("Tuple ([1, 2, 3]) is Unhashable because it contains a mutable object.")
