'''
Write a Python function that calculates the determinant of a 4x4 matrix using Laplace's Expansion method. 
The function should take a single argument, a 4x4 matrix represented as a list of lists, and return the determinant of the matrix. 
The elements of the matrix can be integers or floating-point numbers. 
Implement the function recursively to handle the computation of determinants for the 3x3 minor matrices.
'''
def determinant_4x4(matrix: list[list[int|float]]) -> float:
    if len(matrix) == 1:
        return matrix[0][0]
    det = 0
    for c in range(len(matrix)):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]  
        cofactor = ((-1)**c) * determinant_4x4(minor)  
        det += matrix[0][c] * cofactor  
    return det
