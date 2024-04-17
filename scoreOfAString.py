# https://leetcode.com/problems/score-of-a-string/description/
class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        totalScore = 0
        for i in range(len(s)-1):
            first, second = s[i], s[i+1]
            totalScore += abs(ord(first) - ord(second))
        
        return totalScore