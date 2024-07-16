'''
Write a Python function that performs linear regression using the normal equation. 
The function should take a matrix X (features) and a vector y (target) as input, 
and return the coefficients of the linear regression model. 
Round your answer to four decimal places, -0.0 is a valid result for rounding a very small number.
'''
import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	X_tr = X.T
	y = np.array(y).reshape(-1, 1)
	theta = np.linalg.inv(X_tr.dot(X)).dot(X_tr).dot(y) # вычисление обратной матрицы, как в формуле
	theta = np.round(theta, 4).flatten() # используется для преобразования массива в одномерный вектор
	if len(theta) == 2:
		print(f"The linear model is y = {thate[0] + {theta[1]}*x, perfectly fitteng the input data.")
	else:
		model = f"The linear model is y = {theta[0]}"
		for i in range(1, len(theta)):
			model += f" + {theta[i]}*x_{i}"
		print(model)
	return theta.tolist()
