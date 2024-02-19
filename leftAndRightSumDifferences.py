# https://leetcode.com/problems/left-and-right-sum-differences/description/
class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = nums[:]
        leftSum, rightSum = [], []
        leftPrefix, rightPrefix = 0, 0

        for i in range(len(nums)):
            leftSum.append(leftPrefix)
            leftPrefix += nums[i]

        rightSum = leftSum[:]

        for i in reversed(range(len(nums))):
            rightSum[i] = rightPrefix
            rightPrefix += nums[i]
        
        for i in range(len(nums)):
            answer[i] = abs(leftSum[i] - rightSum[i])
        
        return answer