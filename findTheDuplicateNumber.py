# https://leetcode.com/problems/find-the-duplicate-number/description/?envType=daily-question&envId=2024-04-10
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = {}

        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                return num