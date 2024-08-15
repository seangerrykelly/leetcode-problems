# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/description/
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        opCount = 0
        
        while min(nums) < k:
            minIndex = nums.index(min(nums))
            if nums[minIndex] < k:
                nums.pop(minIndex)
                opCount += 1
        
        return opCount
        