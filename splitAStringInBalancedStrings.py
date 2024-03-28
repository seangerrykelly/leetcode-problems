class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        balanceMap = { 'L': 1, 'R': -1 }
        balance = 0
        count = 0

        for i in range(len(s)):
            curr = s[i]
            balance += balanceMap[curr]
            if balance == 0:
                count += 1
        
        return count