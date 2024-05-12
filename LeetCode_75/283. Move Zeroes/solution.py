'''
TO DO: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        position_for_element = 0 
        for current_element in range(len(nums)):
            if nums[current_element] != 0:
                nums[current_element], nums[position_for_element] = nums[position_for_element], nums[current_element]
                position_for_element += 1
        return nums
