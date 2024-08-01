'''
Write a Python function that performs feature scaling on a dataset using both standardization and min-max normalization. 
The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. 
It should return two 2D NumPy arrays: one scaled by standardization and one by min-max normalization. 
Make sure all results are rounded to the nearest 4th decimal.
'''
import numpy as np

def feature_scaling(data):
  data = np.array(data)

  # Стандартизация
  mean = np.mean(data, axis=0)
  std = np.std(data, axis=0)
  
  std[std == 0] = 1 # Случай, когда все значения одинаковы
  
  z = (data - mean) / std
  
  # Нормализация
  min_value = np.min(data, axis=0)
  max_value = np.max(data, axis=0)
  
  range_value = max_value - min_value
  range_value[range_value == 0] = 1
  
  result = (data - min_value) / range_value
  
  return np.round(z, 4).tolist(), np.round(result, 4).tolist()
