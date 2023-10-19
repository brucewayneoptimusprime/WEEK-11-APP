def matrix_multiply(matrix1, matrix2):
    # Check if matrices are compatible for multiplication
    if len(matrix1[0]) != len(matrix2):
        return "Matrix dimensions are not compatible for multiplication."
    
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Example usage:
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]
result = matrix_multiply(matrix1, matrix2)
if isinstance(result, str):
    print(result)
else:
    for row in result:
        print(row)
