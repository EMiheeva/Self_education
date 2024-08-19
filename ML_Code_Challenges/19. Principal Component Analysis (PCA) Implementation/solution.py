'''
Write a Python function that performs Principal Component Analysis (PCA) from scratch. 
The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. 
The function should standardize the dataset, compute the covariance matrix, find the eigenvalues and eigenvectors, 
and return the principal components (the eigenvectors corresponding to the largest eigenvalues). 
The function should also take an integer k as input, representing the number of principal components to return.
'''
import numpy as np

def pca(data, k):
    data_standardized = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
    
    covariance_matrix = np.cov(data_standardized, rowvar=False)
    
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues_sorted = eigenvalues[idx]
    eigenvectors_sorted = eigenvectors[:,idx]
    
    principal_components = eigenvectors_sorted[:, :k]
    
    return np.round(principal_components, 4).tolist()
