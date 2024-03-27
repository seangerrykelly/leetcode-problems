#https://leetcode.com/problems/count-of-matches-in-tournament/description/
class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0

        while n > 1:
            isEven = n % 2 == 0
            if isEven:
                gameCount = n / 2
                teamsLeft = n / 2
                result += gameCount
                n = teamsLeft
            else:
                gameCount = (n - 1) / 2
                teamsLeft = (n - 1) / 2 + 1
                result += gameCount
                n = teamsLeft
        
        return result
