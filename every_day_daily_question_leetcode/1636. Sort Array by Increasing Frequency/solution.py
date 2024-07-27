from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums) #подсчитали частоты элементов

        def sorting(x):
            return (frequency[x], -x)
        
        nums.sort(key = sorting)
        return nums
