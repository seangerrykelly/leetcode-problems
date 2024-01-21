# https://leetcode.com/problems/maximum-ice-cream-bars/description/
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        iceCreamCount = 0
        costs.sort()
        for cost in costs:
            if coins == 0:
                break
            if cost <= coins:
                iceCreamCount += 1
                coins -= cost
        return iceCreamCount
