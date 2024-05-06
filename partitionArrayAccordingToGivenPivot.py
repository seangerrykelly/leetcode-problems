# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        pivotArr = []
        lower, greater = [], []

        for num in nums:
            if num < pivot:
                lower.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                pivotArr.append(num)
        
        return lower + pivotArr + greater
        