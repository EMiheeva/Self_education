'''
TO DO: Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]

Example 2:
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
'''
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        answer_1 = []
        answer_2 = []
        for i in range(len(nums1)):
            if nums1[i] not in set_2:
                answer_1.append(nums1[i])
                set_2.add(nums1[i]) # чтобы избежать повторного добавления
        for i in range(len(nums2)):
            if nums2[i] not in set_1:
                answer_2.append(nums2[i])
                set_1.add(nums2[i]) # чтобы избежать повторного добавления
        return [answer_1, answer_2]
