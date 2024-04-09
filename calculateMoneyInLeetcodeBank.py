# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/?envType=daily-question&envId=2024-04-07
class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        balance = 0
        deposit = 1
        dayOfWeek = 0

        for i in range(1, n + 1):
            if dayOfWeek == 7:
                deposit += 1
                dayOfWeek = 0
            balance += deposit + dayOfWeek
            dayOfWeek += 1
        
        return balance