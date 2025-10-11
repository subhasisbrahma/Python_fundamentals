"""Demonstrates basic NumPy array creation and operations."""

import numpy as np

# 1. SCALAR (0-D Array): A single value. No brackets needed.
a = np.array(45)

# 2. VECTOR (1-D Array): A list of values. One set of brackets.
b = np.array([1, 2, 3, 4, 5])

# 3. MATRIX (2-D Array): A list of lists (like rows and columns). Two sets of brackets.
c = np.array([[1, 2, 3], [4, 5, 6]])

# 4. TENSOR (3-D Array): A list of 2-D arrays. Three sets of brackets.
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# --- Output: Value and Dimension ---
# ndim is the number of axes (dimensions) of the array.

print(f"Array a: {a}, Dimensions: {a.ndim}")
# Output: Array a: 45, Dimensions: 0

print(f"Array b: {b}, Dimensions: {b.ndim}")
# Output: Array b: [1 2 3 4 5], Dimensions: 1

print(f"Array c:\n{c}\nDimensions: {c.ndim}")
# Output: Array c: [[1 2 3] [4 5 6]], Dimensions: 2

print(f"Array d:\n{d}\nDimensions: {d.ndim}")
# Output: Array d: [[[1 2 3] [4 5 6]] [[1 2 3] [4 5 6]]], Dimensions: 3