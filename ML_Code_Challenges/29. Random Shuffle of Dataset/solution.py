'''
Write a Python function to perform a random shuffle of the samples in two numpy arrays, X and y, 
while maintaining the corresponding order between them. 
The function should have an optional seed parameter for reproducibility.
'''
import numpy as np

def shuffle_data(X, y, seed=None):
    if seed is not None:
      np.random.seed(seed)
    
    if X.shape[0] != y.shape[0]:
      raise ValueError("Количество выборок по X и y должно быть одинаковым.")
    
    # генерируем случайные индексы для перетасовки
    indices = np.arange(X.shape[0])  # создаем массив индексов от 0 до количества образцов
    np.random.shuffle(indices)  # перетасовываем индексы
    
    # перетасовываем X и y с использованием случайных индексов
    X_shuffled = X[indices]
    y_shuffled = y[indices]
    
    return X_shuffled, y_shuffled
