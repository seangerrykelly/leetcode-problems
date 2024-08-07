# https://leetcode.com/problems/sum-of-squares-of-special-elements/description/
class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        specialSum = 0
        n = len(nums)
        for i in range(len(nums)):
            curr = nums[i]
            isSpecial = n % (i+1) == 0
            if isSpecial:
                specialSum += curr**2
        
        return specialSum