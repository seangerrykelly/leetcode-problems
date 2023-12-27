# https://leetcode.com/problems/first-letter-to-appear-twice/description/
class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        letterCounts = {}
        for c in s:
            if c in letterCounts:
                return c
            else:
                letterCounts[c] = 1