# https://leetcode.com/problems/binary-search/description/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        targetIndex = -1
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                break
        return -1
