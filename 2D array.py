import numpy as np
matrix_A = np.array([
    [1, 3, 4],
    [2, 4, 5],
    [6, 7, 8]
])

matrix_B_identity = np.identity(matrix_A.shape[0])

matrix_addition_result = matrix_A + matrix_B_identity

matrix_multiplication_result = np.dot(matrix_A, matrix_B_identity)

print("Matrix A:")
print(matrix_A)

print("\nIdentity Matrix B:")
print(matrix_B_identity)

print("\nMatrix Addition Result:")
print(matrix_addition_result)

print("\nMatrix Multiplication Result:")
print(matrix_multiplication_result)