# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description/?envType=daily-question&envId=2025-06-12
class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxDiff = None

        for i in range(len(nums)):
            if i == 0:
                currDiff = abs(nums[i] - nums[-1])
            else:
                currDiff = abs(nums[i] - nums[i-1])
            if maxDiff == None or currDiff > maxDiff:
                maxDiff = currDiff
        
        return maxDiff