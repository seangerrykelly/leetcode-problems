# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        i = 0

        while i < len(nums):
            curr = nums[i]
            if curr == val:
                nums.pop(i)
            else:
                k += 1
                i += 1

        return k