# https://leetcode.com/problems/water-bottles/?envType=daily-question&envId=2024-07-07
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        maxBottles = 0
        bottleCount = 0
        while numBottles > 0:
            numBottles -= 1
            bottleCount += 1
            maxBottles += 1
            if bottleCount == numExchange:
                numBottles += 1
                bottleCount = 0
        
        return maxBottles