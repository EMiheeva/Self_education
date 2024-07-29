'''
Write a Python function that computes the softmax activation for a given list of scores. 
The function should return the softmax values as a list, each rounded to four decimal places.
'''
import math

def softmax(scores: list[float]) -> list[float]:
    exp_scores = [math.exp(score) for score in scores]
    sum_exp_scores = sum(exp_scores)
    probabilities = [round(score / sum_exp_scores, 4) for score in exp_scores]
    return probabilities
