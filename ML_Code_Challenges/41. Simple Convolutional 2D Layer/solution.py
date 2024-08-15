'''
In this problem, you need to implement a 2D convolutional layer in Python. This function will process an input matrix using a specified convolutional kernel, padding, and stride.
'''
import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    output_height = (input_height - kernel_height + 2 * padding) // stride + 1
    output_width = (input_width - kernel_width + 2 * padding) // stride + 1

    output_matrix = np.zeros((output_height, output_width))
    padded_input = np.pad(input_matrix, ((padding, padding), (padding, padding)), mode='constant')

    for i in range(output_height):
        for j in range(output_width):
            h_start = i * stride
            h_end = h_start + kernel_height
            w_start = j * stride
            w_end = w_start + kernel_width
            window = padded_input[h_start:h_end, w_start:w_end]
            output_matrix[i, j] = np.sum(window * kernel)
    
    return output_matrix
