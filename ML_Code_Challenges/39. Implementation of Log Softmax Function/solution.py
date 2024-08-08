'''
In machine learning and statistics, the softmax function is a generalization of the logistic function 
that converts a vector of scores into probabilities. 
The log-softmax function is the logarithm of the softmax function, and it is often used for 
numerical stability when computing the softmax of large numbers. 
Given a 1D numpy array of scores, implement a Python function to compute the log-softmax of the array.
'''
# Solution 1
import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    scores = np.array(scores)
    max_score = np.max(scores)
    stabilized_scores = scores - max_score
    exponent_scores = np.exp(stabilized_scores)
    sum_exponent_scores = np.sum(exponent_scores)
    softmax_scores = exponent_scores / sum_exponent_scores
    return np.log(softmax_scores)

# Solution 2
import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    # Subtract the maximum value for numerical stability
    scores = scores - np.max(scores)
    return scores - np.log(np.sum(np.exp(scores)))
