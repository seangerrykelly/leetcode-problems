# https://leetcode.com/problems/count-asterisks/description/
class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        asteriskCount = 0
        inPair = False
        for letter in s:
            if letter == '|':
                inPair = not inPair
            elif letter == '*' and inPair == False:
                asteriskCount += 1
        
        return asteriskCount
