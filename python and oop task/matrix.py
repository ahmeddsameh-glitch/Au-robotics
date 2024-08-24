def rotate_matrix_90(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix

def rotate_matrix(matrix, degrees):
    degrees = int(degrees)  
    if degrees == 0:
        return matrix
    elif degrees == 90:
        return rotate_matrix_90(matrix)
    elif degrees == 180:
        matrix = rotate_matrix_90(matrix)
        return rotate_matrix_90(matrix)
    elif degrees == 270:
        matrix = rotate_matrix_90(matrix)
        matrix = rotate_matrix_90(matrix)
        return rotate_matrix_90(matrix)
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original matrix:")
for row in original_matrix:
    print(row)
degrees = input("Enter the degree you want it to be rotated with: ")
rotated_matrix = rotate_matrix(original_matrix, degrees)
print("Rotated matrix:")
for row in rotated_matrix:
    print(row)

