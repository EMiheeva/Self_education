'''
Write a Python function that multiplies a matrix by a scalar and returns the result.
'''
# Solution 1
def scalar_multiply(matrix: list[list[int | float]], scalar: int | float) -> list[list[int | float]]:
    result_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element * scalar)
        result_matrix.append(new_row)

    return result_matrix

# Solution 2
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    return [[element * scalar for element in row] for row in matrix]
