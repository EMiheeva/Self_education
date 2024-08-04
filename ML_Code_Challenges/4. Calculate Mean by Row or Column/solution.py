'''
Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. 
The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.
'''
def calculate_matrix_mean(matrix, mode):
    if mode not in ['row', 'column']:
        raise ValueError("Mode must be 'row' or 'column'")

    if mode == 'row':
        means = [sum(row) / len(row) for row in matrix]

    else:  
        transposed_matrix = list(zip(*matrix))
        means = [sum(col) / len(col) for col in transposed_matrix]
    return means
print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'column'))
