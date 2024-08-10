'''
Write a Python function that calculates the covariance matrix from a list of vectors. 
Assume that the input list represents a dataset where each vector is a feature, and vectors are of equal length.
'''
# Solution 1
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)
    n_observations = len(vectors[0])
    covariance_matrix = [[0 for i in range(n_features)] for i in range(n_features)]

    means = [sum(feature) / n_observations for feature in vectors]

    for i in range(n_features):
        for j in range(i, n_features):
            covariance = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(n_observations)) / (n_observations - 1)
            covariance_matrix[i][j] = covariance_matrix[j][i] = covariance

    return covariance_matrix

# Solution 2
import numpy as np

def calculate_covariance_matrix(vectors):
    
    data = np.array(vectors)
    covariance_matrix = np.cov(data, rowvar=True, bias=False)
    return covariance_matrix.tolist()
