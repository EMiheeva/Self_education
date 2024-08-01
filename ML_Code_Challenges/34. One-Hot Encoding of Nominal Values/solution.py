'''
Write a Python function to perform one-hot encoding of nominal values. 
The function should take in a 1D numpy array x of integer values and an optional integer n_col 
representing the number of columns for the one-hot encoded array. 
If n_col is not provided, it should be automatically determined from the input array.
'''
import numpy as np

def to_categorical(x, n_col=None):
    if n_col is None:
        n_col = np.max(x) + 1
    
    one_hot = np.eye(n_col)[x]
    
    return one_hot
