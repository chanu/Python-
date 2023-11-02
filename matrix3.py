matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_B_ones = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
matrix_addition_result = [[0 for j in range(len(matrix_A[0]))] for i in range(len(matrix_A))]
matrix_multiplication_result = [[0 for j in range(len(matrix_A[0]))] for i in range(len(matrix_A))]
for i in range(len(matrix_A)):
    for j in range(len(matrix_A[0])):
        matrix_addition_result[i][j] = matrix_A[i][j] + matrix_B_ones[i][j]
for i in range(len(matrix_A)):
    for j in range(len(matrix_B_ones[0])):
        for k in range(len(matrix_B_ones)):
            matrix_multiplication_result[i][j] += matrix_A[i][k] * matrix_B_ones[k][j]
print("Matrix A:")
for row in matrix_A:
    print(row)

print("\nOnes Matrix B:")
for row in matrix_B_ones:
    print(row)

print("\nMatrix Addition Result:")
for row in matrix_addition_result:
    print(row)

print("\nMatrix Multiplication Result:")
for row in matrix_multiplication_result:
    print(row)