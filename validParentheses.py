# https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracketMap = { '(': ')', '{': '}', '[': ']'}

        for bracket in s:
            if bracket in bracketMap:
                stack.append(bracket)
            else:
                if len(stack) > 0 and bracket == bracketMap[stack[-1]]:
                    stack.pop()
                    continue
                else:
                    return False
        
        return len(stack) == 0

