'''
Write a Python function to divide a dataset based on whether the value of a specified feature is greater than or equal to a given threshold. 
The function should return two subsets of the dataset: one with samples that meet the condition and another with samples that do not.
'''
import numpy as np

def divide_on_feature(X, feature_i, threshold):
    split_func = None
    if isinstance(threshold, int) or isinstance(threshold, float):
        split_func = lambda sample: sample[feature_i] >= threshold
    else:
        split_func = lambda sample: sample[feature_i] == threshold

    subset_1 = np.array([sample for sample in X if split_func(sample)])
    subset_2 = np.array([sample for sample in X if not split_func(sample)])

    return [subset_1, subset_2]
    
