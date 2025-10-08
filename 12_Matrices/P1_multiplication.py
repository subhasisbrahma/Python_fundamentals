"""Manual multiplication of two 3x3 matrices using triple nested loops."""

# 1. Define the matrices
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

# 2. Initialize the result matrix
result_matrix = [[0, 0, 0] for _ in range(3)]  # 3x3 zero matrix

# 3. Perform multiplication
for i in range(3):          # rows of A
    for j in range(3):      # columns of B
        for k in range(3):  # summation over row i of A and column j of B
            result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

# 4. Print the results

for row in matrix_a:
    print(row)

for row in matrix_b:
    print(row)

for row in result_matrix:
    print(row)

# Expected Output: [25, 12, 10] [58, 30, 25] [91, 48, 40]
