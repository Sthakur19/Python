# Write a Python function that takes a 2D matrix as input and returns its transpose.
# The transpose of a matrix is obtained by interchanging its rows and columns. For example:

# Input matrix
matrix = [[1, 2, 3], 
          [4, 5, 6]]
# Transpose of the matrix
# transposed_matrix = [[1, 4], [2, 5], [3, 6]]

def transposed_matrix(matrix):
    transpose_row = len(matrix[0])
    transpose_col = len(matrix)
    transpose_new_matrix = []
    for i in range(transpose_row):
        transpose_new_matrix_row = []
        for j in range(transpose_col):
            transpose_new_matrix_row.append(0)
        transpose_new_matrix.append(transpose_new_matrix_row)

    transposedMatrixRows = len(transpose_new_matrix)
    transposedMatrixColumns = len(transpose_new_matrix[0])

    for i in range(transposedMatrixRows):
        for j in range(transposedMatrixColumns):
            transpose_new_matrix[i][j] = matrix[j][i]

    return transpose_new_matrix

print(transposed_matrix(matrix))