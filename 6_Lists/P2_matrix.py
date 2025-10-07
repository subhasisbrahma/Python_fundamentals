"""Implements a simple matrix representation using lists."""

# Create the 3x3 matrix (a list where each element is another list/row).
matrix = []
matrix.append([1, 2, 3])  # Row 0
matrix.append([4, 5, 6])  # Row 1
matrix.append([7, 8, 9])  # Row 2

print("Full Matrix (M):", matrix)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing an element with a single index returns the entire row (which is a list).
print("Row 0:", matrix[0])  # Output: [1, 2, 3]
print("Row 1:", matrix[1])  # Output: [4, 5, 6]
print("Row 2:", matrix[2])  # Output: [7, 8, 9]

# The first index is the ROW; the second index is the COLUMN.

# Row 0 (First Row)
print("M[0][0] (R1, C1):", matrix[0][0])  # Output: 1
print("M[0][1] (R1, C2):", matrix[0][1])  # Output: 2
print("M[0][2] (R1, C3):", matrix[0][2])  # Output: 3

# Row 1 (Second Row)
print("M[1][0] (R2, C1):", matrix[1][0])  # Output: 4
print("M[1][1] (R2, C2):", matrix[1][1])  # Output: 5
print("M[1][2] (R2, C3):", matrix[1][2])  # Output: 6

# Row 2 (Third Row)
print("M[2][0] (R3, C1):", matrix[2][0])  # Output: 7
print("M[2][1] (R3, C2):", matrix[2][1])  # Output: 8
print("M[2][2] (R3, C3):", matrix[2][2])  # Output: 9

# Diagonal elements occur where the Row Index == Column Index.
print("M[0][0] (Top-Left):", matrix[0][0])       # Output: 1
print("M[1][1] (Center):", matrix[1][1])         # Output: 5
print("M[2][2] (Bottom-Right):", matrix[2][2])   # Output: 9

