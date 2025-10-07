"""Compares lists and tuples."""

# 1. Immutability Demonstration

# Tuples are defined using parentheses and are IMMUTABLE.
sample_tuple = (1, 2, 3)
print(f"Tuple: {sample_tuple}, Type: {type(sample_tuple)}")

# Note: If you were to try sample_tuple[0] = 99, Python would raise a TypeError
# because tuples cannot be modified after creation.

# Like lists, tuples can be iterated over and support basic indexing/slicing.
print(f"Tuple Index 1: {sample_tuple[1]}") # Output: 2


# 2. Memory Size Comparison

# Create containers with the same number of elements for a fair comparison.
list_data = list(range(10))
tuple_data = tuple(range(10))

print(f"List Data: {list_data}")
print(f"Tuple Data: {tuple_data}")

# __sizeof__() returns the actual memory consumption in bytes.
# Tuples often use less memory because they are immutable and require less overhead.
list_size = list_data.__sizeof__()
tuple_size = tuple_data.__sizeof__()

print(f"\nSize of List (10 elements): {list_size} bytes") 
print(f"Size of Tuple (10 elements): {tuple_size} bytes")

# Conclusion: Tuples are faster and more memory-efficient when the data is fixed.
if list_size > tuple_size:
    print("Observation: The List takes up more space due to mutability overhead.")
