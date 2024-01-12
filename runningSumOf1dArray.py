# https://leetcode.com/problems/running-sum-of-1d-array/description/
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if i == 0:
                continue
            prev = nums[i - 1]
            nums[i] += prev
        return nums