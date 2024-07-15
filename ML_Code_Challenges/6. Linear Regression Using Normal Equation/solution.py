'''
Write a Python function that performs linear regression using the normal equation. 
The function should take a matrix X (features) and a vector y (target) as input, 
and return the coefficients of the linear regression model. 
Round your answer to four decimal places, -0.0 is a valid result for rounding a very small number.
'''
import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
	  X_transpose = X.T
    y = np.array(y).reshape(-1, 1)
	  theta = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)
    theta = np.round(theta, 4).flatten().tolist()
    return theta
