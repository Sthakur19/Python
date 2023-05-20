# Write a Python function that takes a 2D matrix and a scaling factor as input.
# The function should return a new matrix that is obtained by scaling each element of the original
# matrix by the given factor. For example:

# Input matrix
matrix = [[1, 2], [3, 4]]

# Scaling factor
scale_factor = 2

# Output matrix
# Each element is multiplied by the scaling factor
# scaled_matrix = [[2, 4], [6, 8]]

def matrix_scale(matrix, scale):
    matrix_row = len(matrix)
    matrix_col = len(matrix[0])
    # matrix_with_scale_factor = []

    # for i in range(matrix_row):
    #     matrix_with_scale_factor_row = []
    #     for j in range(matrix_col):
    #         matrix_with_scale_factor_row.append(0)
    #     matrix_with_scale_factor.append(matrix_with_scale_factor_row)

    for i in range(matrix_row):
        for j in range(matrix_col):
            matrix[i][j] *= scale
    
    print(matrix)

matrix_scale(matrix, scale_factor)