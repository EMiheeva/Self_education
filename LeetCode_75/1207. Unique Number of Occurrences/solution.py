'''
TO DO: Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2]
Output: false

Example 2:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''
# Without Sets and Maps
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        elements = []
        i = 0
        while i < len(arr):
            current_element = 1
            while i + 1 < len(arr) and arr[i] == arr[i+1]:
                current_element += 1
                i += 1
            elements.append(current_element)
            i += 1
        elements.sort()
        for i in range(1, len(elements)):
            if elements[i] == elements[i-1]:
                return False
        return True

# With Sets and Maps
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequence = {} # словарь для хранения частот элементов
        for x in arr:
            frequence[x] = frequence.get(x, 0) + 1 # втроенный метод get для словаря, чтобы найти элемент и возвращает 0, если такого нет

        return len(frequence) == len(set(frequence.values())) # Логическое выражение, возвращающее True или False!
