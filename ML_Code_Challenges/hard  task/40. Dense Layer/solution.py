'''
You are provided with a base Layer class that defines the structure of a neural network layer. Your task is to implement a subclass called Dense, which represents a fully connected neural network layer. The Dense class should extend the Layer class and implement the following methods:

Initialization (__init__):
    Define the layer with a specified number of neurons (n_units) and an optional input shape (input_shape).
    Set up placeholders for the layer's weights (W), biases (w0), and optimizers.
Weight Initialization (initialize):
    Initialize the weights W using a uniform distribution with a limit of 1 / sqrt(input_shape[0]), and bias w0 should be set to zero
    Initialize optimizers for W and w0.
Parameter Count (parameters):
    Return the total number of trainable parameters in the layer, which includes the parameters in W and w0.
Forward Pass (forward_pass):
    Compute the output of the layer by performing a dot product between the input X and the weight matrix W, and then adding the bias w0.
Backward Pass (backward_pass):
    Calculate and return the gradient with respect to the input.
    If the layer is trainable, update the weights and biases using the optimizer's update rule.
Output Shape (output_shape):
    Return the shape of the output produced by the forward pass, which should be (self.n_units,).
Objective: Extend the Layer class by implementing the Dense class to ensure it functions correctly within a neural network framework.
'''
import numpy as np
import copy
import math

# DO NOT CHANGE SEED
np.random.seed(42)

# DO NOT CHANGE LAYER CLASS
class Layer(object):

    def set_input_shape(self, shape):
        
        self.input_shape = shape

    def layer_name(self):
        return self.__class__.__name__

    def parameters(self):
        return 0

    def forward_pass(self, X, training):
        raise NotImplementedError()

    def backward_pass(self, accum_grad):
        raise NotImplementedError()

    def output_shape(self):
        raise NotImplementedError()

# SOLUTION HERE
class Dense(Layer):
    def __init__(self, n_units, input_shape=None):
        self.layer_input = None
        self.input_shape = input_shape
        self.n_units = n_units
        self.trainable = True
        self.W = None
        self.w0 = None

    def initialize(self, optimizer):
        limit = 1 / math.sqrt(self.input_shape[0])
        self.W  = np.random.uniform(-limit, limit, (self.input_shape[0], self.n_units))
        self.w0 = np.zeros((1, self.n_units))
        self.W_opt  = copy.copy(optimizer)
        self.w0_opt = copy.copy(optimizer)

    def parameters(self):
        return np.prod(self.W.shape) + np.prod(self.w0.shape)

    def forward_pass(self, X, training=True):
        self.layer_input = X
        return X.dot(self.W) + self.w0

    def backward_pass(self, accum_grad):
        W = self.W
        if self.trainable:
            grad_w = self.layer_input.T.dot(accum_grad)
            grad_w0 = np.sum(accum_grad, axis=0, keepdims=True)
            self.W = self.W_opt.update(self.W, grad_w)
            self.w0 = self.w0_opt.update(self.w0, grad_w0)
        accum_grad = accum_grad.dot(W.T)
        return accum_grad

    def output_shape(self):
        return (self.n_units, )
    
