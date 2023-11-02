rows = 3
columns = 4
matrix_A = [[0 for j in range(columns)] for i in range(rows)]
for i in range(rows):
    for j in range(columns):
        matrix_A[i][j] = i * columns + j + 1
print("Matrix A:")
for row in matrix_A:
    print(row)