'''
Write a Python function to calculate the correlation matrix for a given dataset. 
The function should take in a 2D numpy array X and an optional 2D numpy array Y. 
If Y is not provided, the function should calculate the correlation matrix of X with itself. 
It should return the correlation matrix as a 2D numpy array.
'''
import numpy as np

def calculate_correlation_matrix(X, Y=None):
    if Y is None:
      Y = X
      
    def calculate_std_dev(A):
        return np.sqrt(np.mean((A - A.mean(0))**2, axis=0))
      
    n_samples = np.shape(X)[0]

    covariance_matrix = (1 / n_samples) * (X - X.mean(0)).T.dot(Y - Y.mean(0))

    std_dev_X = np.expand_dims(calculate_std_dev(X), 1)
    std_dev_y = np.expand_dims(calculate_std_dev(Y), 1)

    correlation_matrix = np.divide(covariance_matrix, std_dev_X.dot(std_dev_y.T))

    return np.array(correlation_matrix, dtype=float)
    
