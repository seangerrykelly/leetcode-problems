# https://leetcode.com/problems/apply-operations-to-an-array/description/
class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        zeroCount = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                zeroCount += 1
                nums.pop(i)
            else:
                i += 1
        
        return nums + [0 for i in range(zeroCount)]
        