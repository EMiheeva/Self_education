'''
Write a Python function to generate random subsets of a given dataset. 
The function should take in a 2D numpy array X, a 1D numpy array y, an integer n_subsets, and a boolean replacements. 
It should return a list of n_subsets random subsets of the dataset, where each subset is a tuple of (X_subset, y_subset). 
If replacements is True, the subsets should be created with replacements; otherwise, without replacements.
'''
import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True,seed=42):
    np.random.seed(seed)
    n_samples = np.shape(X)[0]
    X_y = np.concatenate((X, y.reshape((len(y), 1))), axis=1)
    np.random.shuffle(X_y)
    subsets = []
	
    for element in range(n_subsets):
      if replacements:
        subsample_size = n_samples
      else:
        subsample_size = n_samples // 2

    for element in range(n_subsets):
        idx = np.random.choice(
            range(n_samples),
            size=subsample_size,
            replace=replacements)
        X_subset = X_y[idx][:,:-1]
        y_subset = X_y[idx][:,-1]
        subsets.append([X_subset, y_subset])
    return subsets
    
