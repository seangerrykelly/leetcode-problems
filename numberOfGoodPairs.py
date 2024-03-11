# https://leetcode.com/problems/number-of-good-pairs/description/
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = {}
        numPairs = 0

        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                numMap[num] += 1
        
        for num in numMap:
            n = numMap[num]
            numPairs += n*(n-1)//2
        
        return numPairs
