class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxWealth = 0
        for customer in accounts:
            customerWealth = 0
            for account in customer:
                customerWealth += account
            if customerWealth > maxWealth:
                maxWealth = customerWealth
        
        return maxWealth