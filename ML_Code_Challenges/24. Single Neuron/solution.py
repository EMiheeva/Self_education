'''
Write a Python function that simulates a single neuron with a sigmoid activation function for binary classification, 
handling multidimensional input features. The function should take a list of feature vectors (each vector representing 
multiple features for an example), associated true binary labels, 
and the neuron's weights (one for each feature) and bias as input. 
It should return the predicted probabilities after sigmoid activation and the mean squared error 
between the predicted probabilities and the true labels, both rounded to four decimal places.
'''
import math
def single_neuron_model(features, labels, weights, bias):
    probabilities = []
    for feature_vector in features:
      z = 0
      for i in range(len(weights)):
        z += weights[i] * feature_vector[i]
      z += bias
      prob = 1 / (1 + math.exp(-z))
      probabilities.append(round(prob, 4))

    mse = 0
    for i in range(len(probabilities)):
      mse += (probabilities[i] - labels[i]) ** 2
    mse /= len(labels)
    mse = round(mse, 4)
    
    return probabilities, mse
