'''
Write a Python function that uses the Jacobi method to solve a system of linear equations given by Ax = b. The function should iterate 10 times, 
rounding each intermediate solution to four decimal places, and return the approximate solution x.
'''
# Solution 1
import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:

    size = A.shape[0]
    x = np.zeros(size)
    
    x_new = np.zeros(size)
    for iteration in range(n):
        for i in range(size):
            sum_ax = sum(A[i][j] * x[j] for j in range(size) if j != i)
            # Формула Якоби
            x_new[i] = (b[i] - sum_ax) / A[i][i]
        x_new = np.round(x_new, 4)
        x = x_new.copy()
    return x.tolist()
  # Solution 2
  import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    d_a = np.diag(A)
    nda = A - np.diag(d_a)
    x = np.zeros(len(b))
    x_hold = np.zeros(len(b))
    for _ in range(n):
        for i in range(len(A)):
            x_hold[i] = (1/d_a[i]) * (b[i] - sum(nda[i]*x))
        x = x_hold.copy()
    return np.round(x,4).tolist()
