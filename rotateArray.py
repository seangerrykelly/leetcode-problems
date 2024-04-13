# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        positionMap = {}
        for i in range(len(nums)):
            num = nums[i]
            newPosition = i + (k % len(nums))
            if newPosition > len(nums) - 1:
                newPosition -= len(nums)
            positionMap[newPosition] = num

        for i in range(len(nums)):
            nums[i] = positionMap[i]