# https://leetcode.com/problems/contains-duplicate/submissions/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicateMap = {}
        for num in nums:
            if num not in duplicateMap:
                duplicateMap[num] = 1
            else:
                return True
        return False
        