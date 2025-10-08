"""Implements 3x3 matrix multiplication using reusable functions for clarity."""

# 1. Helper Functions
def initialize_mat(dim):
    """Initialize an N x N zero matrix."""
    return [[0 for _ in range(dim)] for _ in range(dim)]

def dot_product(u, v):
    """Compute dot product of two vectors."""
    return sum(u[i] * v[i] for i in range(len(u)))

def get_row(matrix, row_index):
    """Return the specified row from a matrix."""
    return matrix[row_index]

def get_column(matrix, col_index):
    """Return the specified column from a matrix."""
    return [matrix[i][col_index] for i in range(len(matrix))]

def mat_mul(matrix_a, matrix_b):
    """Multiply two square matrices using dot product."""
    dim = len(matrix_a)
    result = initialize_mat(dim)
    
    for i in range(dim):
        for j in range(dim):
            result[i][j] = dot_product(get_row(matrix_a, i), get_column(matrix_b, j))
    
    return result

matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_b = [
    [1, 2, 1],
    [6, 2, 3],
    [4, 2, 1]
]
print(mat_mul(matrix_a,matrix_b))
# Expected Output: [[25, 12, 10], [58, 30, 25], [91, 48, 40]]
