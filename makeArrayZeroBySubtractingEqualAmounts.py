# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/
class Solution(object):
    def getSmallestNum(self, nums):
        smallestNum = 0
        for i in range(len(nums)):
            if smallestNum == 0 and nums[i] > 0:
                smallestNum = nums[i]
            elif nums[i] != 0 and nums[i] < smallestNum:
                smallestNum = nums[i]
        return smallestNum

    def decrementArray(self, nums, smallestNum):
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] -= smallestNum
        return nums

    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimumOperations = 0
        while nums.count(0) != len(nums):
            smallestNum = self.getSmallestNum(nums)
            nums = self.decrementArray(nums, smallestNum)
            minimumOperations += 1

        return minimumOperations