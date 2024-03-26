# https://leetcode.com/problems/first-missing-positive/description/?envType=daily-question&envId=2024-03-26
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = {}
        smallest = 0

        for num in nums:
            if num not in numMap:
                numMap[num] = 1
        
        smallest = 0
        while True:
            smallest += 1
            if smallest not in numMap:
                break
            else:
                continue
        
        return smallest

