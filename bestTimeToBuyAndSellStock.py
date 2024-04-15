# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        profit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            currProfit = price - minPrice
            if currProfit > profit:
                profit = currProfit
        
        return profit
