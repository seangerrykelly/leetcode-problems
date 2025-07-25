# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/?envType=daily-question&envId=2025-07-25
class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = 0
        numMap = {}
        isAllNegative = True
        for num in nums:
            if num > 0:
                isAllNegative = False
            if num not in numMap:
                numMap[num] = 1
            else:
                numMap[num] += 1
        
        if isAllNegative:
            return max(nums)
        
        for num in numMap:
            if num > 0:
                maxSum += num
        
        return maxSum
        