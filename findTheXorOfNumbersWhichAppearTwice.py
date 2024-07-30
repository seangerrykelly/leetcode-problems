# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description/
class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = {}
        xor = 0

        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                xor = xor ^ num
        
        return xor
        