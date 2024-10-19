# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/
class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numMap = {}
        sneakyNumbers = []

        for num in nums:
            if num not in numMap:
                numMap[num] = True
            else:
                sneakyNumbers.append(num)
        
        return sneakyNumbers