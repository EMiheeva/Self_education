'''
Write a Python function to calculate the accuracy score of a model's predictions. 
The function should take in two 1D numpy arrays: 
y_true, which contains the true labels, and y_pred, which contains the predicted labels. 
It should return the accuracy score as a float.
'''
import numpy as np

def accuracy_score(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred, axis=0) / len(y_true)
    return accuracy
