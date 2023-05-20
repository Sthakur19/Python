# Rotating a Matrix
# Write a Python function that takes a 2D matrix as
# input and returns a new matrix that is obtained by rotating
# the original matrix 90 degrees clockwise. For example:

# Input matrix
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
# Rotated matrix (90 degrees clockwise)
# rotated_matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

def rotated_matrix(matrix):
    matrix_row = len(matrix)
    matrix_col = len(matrix[0])
    rotated_matrix_full = []
    for i in range(matrix_row):
        rotated_matrix_row = []
        for j in range(matrix_col):
            rotated_matrix_row.append(0)
        rotated_matrix_full.append(rotated_matrix_row)

    for i in range(matrix_row):
        for j in range(matrix_col):
            rotated_matrix_full[i][j] = matrix[matrix_row - j - 1][i]
        
    print(rotated_matrix_full)



rotated_matrix(matrix)