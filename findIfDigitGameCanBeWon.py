# https://leetcode.com/problems/find-if-digit-game-can-be-won/description/
class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        singleSum, doubleSum = 0, 0

        for num in nums:
            if num < 10:
                singleSum += num
            else:
                doubleSum += num
        
        return singleSum != doubleSum