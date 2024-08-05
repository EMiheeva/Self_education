'''
Write a Python function to create a batch iterator for the samples in a numpy array X and an optional numpy array y. 
The function should yield batches of a specified size. If y is provided, the function should yield batches of (X, y) pairs; 
otherwise, it should yield batches of X only.
'''
import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    n_samples = X.shape[0]
    batches = []
    for i in np.arange(0, n_samples, batch_size):
        begin, end = i, min(i+batch_size, n_samples)
        if y is not None:
            batches.append([X[begin:end], y[begin:end]])
        else:
            batches.append( X[begin:end])
    return batches
