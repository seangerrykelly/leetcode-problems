# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/?envType=daily-question&envId=2024-04-04
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxDepth = 0
        currDepth = 0
        bracketMap = {'(': ')'}

        for c in s:
            if c in bracketMap:
                stack.append(c)
                currDepth += 1
                if currDepth > maxDepth:
                    maxDepth = currDepth
            elif c == bracketMap.values()[0]:
                stack.pop()
                currDepth -= 1
            else:
                continue
        
        return maxDepth
