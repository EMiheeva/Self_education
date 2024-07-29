'''
Write a Python function that computes the output of the sigmoid activation function given an input value z. 
The function should return the output rounded to four decimal places.
'''
import math

def sigmoid(z: float) -> float:
    result = 1 / (1 + math.exp(-z))
    return round(result, 4)
