# https://leetcode.com/problems/rotate-string/?envType=daily-question&envId=2024-11-03
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        
        s += s
        for i in range(len(goal)):
            substring = s[i:i+len(goal)]
            if substring == goal:
                return True
        
        return False

