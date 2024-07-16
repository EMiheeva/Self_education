'''
Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector
'''
# n - rows
# m - column
# len(a[0]) = m
# len(b) = m

#Solution 1
def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    if len(a[0]) != len(b):
        return -1
    result = []
    for i in a:
        element_product_matrix = 0
        for j in range(len(i)):
            element_product_matrix += (i[j] * b[j])
        result.append(element_product_matrix)
    return result

#Solution 2
import numpy as np
def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    if len(a[0]) != len(b):
        return -1
    # преобразуем a и b в массивы numpy
    a = np.array(a)
    b = np.array(b) 
    result = np.dot(a,b) #встроенный метод умножения матрицы на вектор
    return result.tolist() #преобразуем к нужному типу данных
