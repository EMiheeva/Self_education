'''
Write a Python function to convert a 1D numpy array into a diagonal matrix. 
The function should take in a 1D numpy array x and return a 2D numpy array representing the diagonal matrix.
'''
#Solution 1
import numpy as np

def make_diagonal(x):
    n = len(x)
    diagonal_matrix = [[0] * n for i in range(n)]
    
    for i in range(n):
      diagonal_matrix[i][i] = x[i]
    return diagonal_matrix

#Solution 2
import numpy as np

def make_diagonal(x):
    identity_matrix = np.identity(np.size(x))
    return (identity_matrix*x)
