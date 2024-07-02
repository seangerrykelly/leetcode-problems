# https://leetcode.com/problems/number-of-distinct-averages/description/
class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        averageMap = {}

        while nums:
            minimum = nums.pop(0)
            maximum = nums.pop()
            average = (minimum + maximum) / 2.0
            if average not in averageMap:
                averageMap[average] = 1
        
        return len(averageMap)
