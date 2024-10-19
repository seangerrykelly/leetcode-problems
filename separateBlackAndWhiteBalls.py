# https://leetcode.com/problems/separate-black-and-white-balls/description/
class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        minSteps = 0
        zeroCounter = 0
        for i in reversed(range(len(s))):
            if s[i] == '0':
                zeroCounter += 1
            elif s[i] == '1':
                minSteps += zeroCounter
        
        return minSteps