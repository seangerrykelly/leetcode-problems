# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        opCount = 0
        for i in range(len(nums)-2):
            curr = nums[i]
            if curr == 0:
                # Flip next 3 elements
                for j in range(3):
                    nums[i+j] = 1 - nums[i+j]
                opCount += 1
        
        if min(nums) == 0:
            return -1
        else:
            return opCount