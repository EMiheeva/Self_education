'''
Write a Python function that reshapes a given matrix into a specified shape.
'''
import numpy as np
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    array = np.array(a)
    
    # Проверка 
    if array.size != new_shape[0] * new_shape[1]:
        raise ValueError("Общее количество элементов в исходной матрице должно соответствовать общему количеству элементов в новой форме.")
    
    reshaped_array = array.reshape(new_shape)
    return reshaped_array.tolist()
