'''
Write a Python function that implements the k-Means algorithm for clustering, starting with specified initial centroids and a set number of iterations. 
The function should take a list of points (each represented as a tuple of coordinates), an integer k representing the number of clusters to form, 
a list of initial centroids (each a tuple of coordinates), and an integer representing the maximum number of iterations to perform. 
The function will iteratively assign each point to the nearest centroid and update the centroids based on the assignments until 
the centroids do not change significantly, or the maximum number of iterations is reached. The function should return a list of 
the final centroids of the clusters. Round to the nearest fourth decimal.
'''
import numpy as np

def euclidean_distance(a, b):
    return np.sqrt(((a - b) ** 2).sum(axis=1))

def k_means_clustering(points, k, initial_centroids, max_iterations):
    points = np.array(points)
    centroids = np.array(initial_centroids)
    
    for iteration in range(max_iterations):
        distances = np.array([euclidean_distance(points, centroid) for centroid in centroids])
        assignments = np.argmin(distances, axis=0)

        new_centroids = np.array([points[assignments == i].mean(axis=0) if len(points[assignments == i]) > 0 else centroids[i] for i in range(k)])
        
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
        centroids = np.round(centroids, 4)
    return [tuple(centroid) for centroid in centroids]
