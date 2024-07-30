# https://leetcode.com/problems/special-array-i/description/
class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        
        isSpecial = True
        for i in range(1, len(nums)):
            prev, curr = nums[i-1], nums[i]
            if (prev % 2 == 0 and curr % 2 == 0) or (prev % 2 != 0 and curr % 2 != 0):
                isSpecial = False
                break
            else:
                continue
        return isSpecial
